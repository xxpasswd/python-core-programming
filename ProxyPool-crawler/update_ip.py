# coding: utf-8
from utils.db_helper import DBHelper
from verify_process.verify_ip import VerifyIp


def process_res():
    """
    验证ip有效性，并处理结果
    :return:
    """
    db = DBHelper()
    ip_list = db.get_all_ips()
    ip_list_copy = ip_list.copy()
    ip_valid_list = []
    threads = []
    # 创建处理ip结果的线程
    for i in range(50):
        threads.append(VerifyIp(ip_list, ip_valid_list))

    # 开始所有线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    for ip in ip_list_copy:
        if ip not in ip_valid_list:
            db.delete_one_ip(ip)
    print(ip_valid_list, len(ip_valid_list))


if __name__ == '__main__':
    print('开始更新数据库中有效的代理ip')
    process_res()
    print('更新完成')
