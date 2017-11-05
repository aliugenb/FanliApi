# __author__ = Roger
# -*- coding: utf-8 -*-
import hashlib


def decrypt_ab(abtest):
    ab_arr = abtest.split('-')
    test_arr = {}
    if len(ab_arr) > 1:
        ab_sig = ab_arr.pop()
        ab_str = '-'.join(ab_arr)
        md5 = hashlib.md5()
        md5.update(ab_str)
        md5_str = md5.hexdigest()
        md5_sig = md5_str[0] + md5_str[2] + md5_str[4] + md5_str[6]
        if ab_sig == md5_sig:
            id_add = 0
            for key in ab_arr:
                key_arr = key.split('_')
                test_id = int(key_arr[0]) + id_add
                test_group = key_arr[1]
                id_add = test_id
                test_arr[test_id] = test_group
    print test_arr

if __name__ == '__main__':
    decrypt_ab('17454_a-1030_a-1228_a-30327_e-66_c-138_b-40_b-9768_d-80_b-12_b-6_b-8_b-4_b-160_a-2088')