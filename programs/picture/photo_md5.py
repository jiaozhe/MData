import os
import hashlib


def file_md5(file_name):
    m = hashlib.md5()
    with open(file_name, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            m.update(chunk)
    return m.hexdigest().upper()


# main
if __name__ == '__main__':
    RNS = ["%03d" % i for i in range(1000)]

    photo_dir = r"D:\Photo\123"
    os.chdir(photo_dir)
    photo_files = [p for p in os.listdir(photo_dir) if os.path.isfile(p)]
    for p in photo_files:
        _tmp_old_name, _tmp_old_ext = os.path.splitext(p)
        _tmp_new_name = file_md5(p)
        _tmp_new_ext = _tmp_old_ext.lower()
        new_name = _tmp_new_name + _tmp_new_ext

        try:
            os.rename(p, new_name)
            print("%s --> %s" % (p, new_name))
        except Exception:
            if os.path.exists(new_name):
                new_name = _tmp_new_name + "_" + RNS.pop(0) + _tmp_new_ext
                os.rename(p, new_name)
                # os.unlink(p)
                print("%s --> %s" % (p, new_name))
            else:
                pass
