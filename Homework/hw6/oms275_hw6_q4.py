from DoublyLinkedList import *
from copy import deepcopy


def copy_linked_list(lnk_lst):
    result_lst = DoublyLinkedList()
    current = lnk_lst.header.next
    while current != lnk_lst.trailer:
        result_lst.add_last(current.data)
        current = current.next
    return result_lst


def deep_copy_linked_list(lnk_lst):
    result_lst = DoublyLinkedList()
    current = lnk_lst.header.next
    while current != lnk_lst.trailer:
        if isinstance(current.data, DoublyLinkedList):
            result_lst.add_last(deepcopy(current.data))
        else:
            result_lst.add_last(current.data)
        current = current.next
    return result_lst
