/*
 * heap.h
 *
 *  Created on: May 2, 2016
 *      Author: geri
 */

#ifndef SRC_INCLUDE_HEAP_H_
#define SRC_INCLUDE_HEAP_H_

#include <vector>

using std::vector;

template <class T>
class Heap
{
public:
	Heap() {}
	Heap(const Heap<T> _other) : _arr(_other._arr) {}
	void insert(const T& val)
	{

	}
private:
	vector<T> _arr;
};



#endif /* SRC_INCLUDE_HEAP_H_ */
