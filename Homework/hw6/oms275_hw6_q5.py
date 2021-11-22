from DoublyLinkedList import *


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    result = DoublyLinkedList()
    current1 = srt_lnk_lst1.header.next
    current2 = srt_lnk_lst2.header.next
    wait = True
    while wait:
        if current1 == srt_lnk_lst1.trailer:
            result.add_last(current2.data)
            current2 = current2.next
        elif current2 == srt_lnk_lst2.trailer:
            result.add_last(current1.data)
            current1 = current1.next
        else:
            if current1.data <= current2.data:
                result.add_last(current1.data)
                current1 = current1.next
            elif current2.data <= current1.data:
                result.add_last(current2.data)
                current2 = current2.next
        if current1 == srt_lnk_lst1.trailer and current2 == srt_lnk_lst2.trailer:
            wait = False
    return result
