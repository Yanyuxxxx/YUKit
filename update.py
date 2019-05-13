# -*- coding: UTF-8 -*-
import os, sys
import fileinput



# ======================  edit by yourself  ======================
sources = [
    'https://github.com/Yanyuxxxx/YURepo.git',
]

project_name = 'YURepo'
podspec_file_name = 'YUKit.podspec'


# ==================================================================



new_tag = ""
lib_command = ""
pod_push_command = ""
spec_file_path = "./" + podspec_file_name
find_version_flag = False



def pod_command_edit():
    global lib_command
    global pod_push_command
    source_suffix = 'https://github.com/CocoaPods/Specs.git --allow-warnings'
    lib_command = 'pod lib lint --sources='
    pod_push_command = 'pod repo pushs ' + project_name + ' ' + podspec_file_name
    if len(sources) > 0:
        # rely on  private sourece
        pod_push_command += ' --sources='

        for index,source in enumerate(sources):
            lib_command += source
            lib_command += ','
            pod_push_command += source
            pod_push_command += ','

        lib_command += source_suffix
        pod_push_command += source_suffix

    else:
        lib_command = 'pod lib lint'


def update_version():
    f = open(spec_file_path, 'r+')
    infos = f.readlines()
    f.seek(0, 0)
    file_data = ""
    new_line = ""
    global find_version_flag
    find_version_flag = False

    for line in infos:
        if line.find(".version") != -1:
            if find_version_flag == False:
                
                # find s.version = "xxxx"
                line_arr0 = line.split('"')
                line_arr1 = line.split("'")
                version_str = ""
                if len(line_arr0) > 2:
                    version_str = line_arr0[1]
                if len(line_arr1) > 2:
                    version_str = line_arr1[1]

                num_arr = version_str.split(".")
                if len(num_arr) != 3:
                	raise RuntimeError("--------- 不支持此类version --------")

                v0 = int(num_arr[0])
                v1 = int(num_arr[1])
                v2 = int(num_arr[2])
                if not(v1 >= 0 and v1 < 10):
                	raise RuntimeError("--------- 不支持此类version --------")
                if not(v2 >= 0 and v2 < 10):
                	raise RuntimeError("--------- 不支持此类version --------")

                # updateVersion
                v2 += 1
                if v2 == 10:
                	v2 = 0
                	v1 += 1
                	if v1 == 10:
                		v1 = 0
                		v0 += 1
                global new_tag
                new_tag = str(v0) + "." + str(v1) + "." + str(v2)

                # complete new_tag
                if len(line_arr0) > 2:
                    line = line_arr0[0] + '"' + new_tag + '"' + '\n'
                if len(line_arr1) > 2:
                    line = line_arr1[0] + "'" + new_tag + "'" + "\n"

                # complete new_line
                print "this is new tag  " + new_tag
                find_version_flag = True

        file_data += line

    with open(spec_file_path, 'w', ) as f1:
        f1.write(file_data)

    f.close()

    print "--------- auto update version -------- "

def recover_version():
    f = open(spec_file_path, 'r+')
    infos = f.readlines()
    f.seek(0, 0)
    file_data = ""
    new_line = ""
    global find_version_flag
    find_version_flag = False

    for line in infos:
        if line.find(".version") != -1:
            if find_version_flag == False:
                
                # find s.version = "xxxx"
                line_arr0 = line.split('"')
                line_arr1 = line.split("'")
                version_str = ""
                if len(line_arr0) > 2:
                    version_str = line_arr0[1]
                if len(line_arr1) > 2:
                    version_str = line_arr1[1]

                num_arr = version_str.split(".")
                if len(num_arr) != 3:
                    raise RuntimeError("--------- 不支持此类version --------")

                v0 = int(num_arr[0])
                v1 = int(num_arr[1])
                v2 = int(num_arr[2])
                if not(v1 >= 0 and v1 < 10):
                    raise RuntimeError("--------- 不支持此类version --------")
                if not(v2 >= 0 and v2 < 10):
                    raise RuntimeError("--------- 不支持此类version --------")

                # updateVersion
                v2 -= 1
                if v2 == -1:
                    v2 = 9
                    v1 -= 1
                    if v1 == -1:
                        v1 = 9
                        v0 -= 1
                        if v0 == -1:
                            raise RuntimeError("--------- version不能小于0 --------")
                global new_tag
                new_tag = str(v0) + "." + str(v1) + "." + str(v2)

                # complete new_tag
                if len(line_arr0) > 2:
                    line = line_arr0[0] + '"' + new_tag + '"' + '\n'
                if len(line_arr1) > 2:
                    line = line_arr1[0] + "'" + new_tag + "'" + "\n"

                # complete new_line
                print "恢复version  " + new_tag
                find_version_flag = True

        file_data += line

    with open(spec_file_path, 'w', ) as f1:
        f1.write(file_data)

    f.close()

    print "--------- recover version -------- "

def lib_lint():
    print("-------- waiting for pod lib lint checking ...... ---------")
    r = os.system(lib_command)
    if r != 0 :
        recover_version()
        raise RuntimeError("--------- lib_lint 失败 --------")

def git_operation():
    os.system('git add .')
    commit_desc = "version_" + new_tag
    commit_command = 'git commit -m "' + commit_desc + '"'
    os.system(commit_command)
    # git push
    r = os.popen('git symbolic-ref --short -q HEAD')
    current_branch = r.read()
    r.close()
    push_command = 'git push origin ' + current_branch
    
    # tag
    tag_delete_command = 'git tag -d ' + new_tag
    os.system(tag_delete_command)

    tag_add_command = 'git tag -m "' + new_tag + '" ' + new_tag
    os.system(tag_add_command)
    
    # push tags
    os.system('git push --tags')

def pod_push():
    print("--------  waiting for pod push  ...... ---------")
    r = os.system(pod_push_command)
    if r != 0 :
        recover_version()
        raise RuntimeError("--------- pod_push 失败 --------")



# run commands
update_version()
pod_command_edit()
lib_lint()
git_operation()
pod_push()


