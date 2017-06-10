/*
 * dynamic.h
 *
 *  Created on: Apr 13, 2016
 *      Author: geri
 */

#ifndef DYNAMIC_H_
#define DYNAMIC_H_

#include <utils.h>
#include <vector>
#include <limits>
#include <algorithm>
#include <chrono>

using std::vector;


class RodCutter
{
public:
	RodCutter(const vector<double>& prices) : 	_prices(prices),
												_length(prices.size()-1),
												_freqs(prices.size(), 0),
												_revenue(prices.size(), std::numeric_limits<int>::min()),
												_functionCalls(0)
	{
	}
	virtual ~RodCutter() {};

	double revenue()
	{
		_startTimePoint = std::chrono::high_resolution_clock::now();
		double result = cutrod(_length);
		_endTimePoint = std::chrono::high_resolution_clock::now();
		return result;
	}

	int getNumOfFunctionCalls() const {return _functionCalls;}

	const vector<int>& getFreqs() const {return _freqs;}
	const vector<double>& getRevenues() const {return _revenue;}

	size_t getMicroSecondCount() {return std::chrono::duration_cast<std::chrono::microseconds>(_endTimePoint-_startTimePoint).count(); }

	virtual double cutrod(int n) = 0;

protected:
	vector<double> _prices;
	vector<int>    _freqs;
	vector<double> _revenue;
	int _length;
	int _functionCalls;
	std::chrono::high_resolution_clock::time_point _startTimePoint;
	std::chrono::high_resolution_clock::time_point _endTimePoint;
};


class ExponentialRodCutter : public RodCutter
{
public:
	ExponentialRodCutter(const vector<double>& prices) : RodCutter(prices) {}
	virtual double cutrod(int n)
	{
		_freqs[n]++;
		_functionCalls++;
		if(n == 0)
			return 0;
		double q = std::numeric_limits<double>::min();
		for(int i=1;i<=n;i++)
		{
			q = std::max(q, _prices[i] + cutrod(n-i));
		}
		_revenue[n] = q;
		return q;
	}
};

class MemoizedRecursiveRodCutter : public RodCutter
{
public:
	MemoizedRecursiveRodCutter(const vector<double>& prices) : RodCutter(prices) {}
	virtual double cutrod(int n)
	{
		if(_revenue[n]>=0)
			return _revenue[n];
		if(n == 0)
			return 0;
		double q = std::numeric_limits<int>::min();
		for(int i=1;i<=n;i++)
		{
			q = std::max(q, _prices[i] + cutrod(n-i));
		}
		_revenue[n] = q;
		return q;

	}
};

class BottomUpRodCutter : public RodCutter
{
public:
	BottomUpRodCutter(const vector<double>& prices) : RodCutter(prices) {}
	virtual double cutrod(int n)
	{
		_revenue[0] = 0;
		for(int j=1;j<=n;j++)
		{
			double q = std::numeric_limits<int>::min();
			for(int i=1;i<=j;i++)
			{
				q = std::max(q, _prices[i] + _revenue[j-i]);
			}
			_revenue[j] = q;
		}
		return _revenue[n];
	}
};


class MatrixChainMultiplier
{
public:
	MatrixChainMultiplier(const vector<int>& dims) : _dims(dims) {}



private:
	vector<int> _dims;
	vector<vector<int>> _costs;				// costs of computing matrix chain [i,j]
	vector<vector<int>> _optimalIndexes;	// optimal index to achive cost m[i,j]

};


#endif /* DYNAMIC_H_ */
