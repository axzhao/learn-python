
echo "This is a Unix shell" | grep -Eo "Unix \w+"

# read param
# echo $param

###########################################################################
###### 脚本输入参数
###########################################################################
:<<EOF
EOF
###########################################################################

echo "\$# 传递到脚本的参数个数 $#"

para="para: ";
while [ $# -ge 2 ] ; do
        case "$1" in
                --startdate) para="${para} argument $1 = $2"; shift 2;;
                --enddate) para="${para} argument $1 = $2"; shift 2;;
                *) echo "unknown parameter $1." ; exit 1 ; break;;
        esac
done

echo $para # para: argument --startdate = 20190926 argument --enddate = 20190926

###########################################################################
###### 变量
###########################################################################
:<<EOF
    脚本在执行时都会启动一个子shell进程, 命令行中启动的脚本会继承当前shell环境变量。
    系统自动启动脚本（非命令行启动）, 则需要自我定义环境变量。
EOF
###########################################################################

# 环境变量, 作用域：当前的shell和其子shell。
export MY_NAME=dev

# 本地变量, 作用域：整个bash进程
localVar="haha" 
echo $localVar # 引用变量：${变量名}，一般可以省略{}
unset localVar # 撤销变量
echo $localVar

# 位置变量
startDate=$1
endDate=$2
echo "\$0 执行的文件名 $0"
echo $startDate
echo $endDate

# 特殊变量
echo "\$# 传递到脚本的参数个数 $#"
echo "\$@ 与\$#相同，使用时加引号，并在引号中返回参数个数 $@"
echo "\$* 传递到脚本的参数，与位置变量不同，此选项参数可超过9个 $*"

echo "\$$ 脚本运行时当前进程的ID号，常用作临时变量的后缀，如 haison.$$"
echo "\$! 后台运行的（&）最后一个进程的ID号 $!"

echo "\$- 上一个命令的最后一个参数 $-"
echo "\$? 最后命令的退出状态，0表示没有错误，其他任何值表明有错误 $?"


echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done

echo "-- 假设在脚本运行时写了参数 1、2，，则 "\*" 等价于 "1 2"（传递了一个参数），而 "\@" 等价于 "1" "2"（传递了两个参数） ---"

###########################################################################
###### 引号
###########################################################################
:<<EOF
    单引号：强引用，不作变量替换
    双引号：弱引用，做变量替换
    反引号：命令替换
EOF
###########################################################################

# 拼接
greeting="hello, "$MY_NAME" !"
greeting_1="hello, ${MY_NAME} !"
echo $greeting  $greeting_1

# 字符串
string="abcd"
echo ${#string} # 长度
string="abcdefg"
echo ${string:1:4}

# 数组
array_name=(value0 value1 value2 value3) # 可断行
array_name[0]=value0
echo ${array_name[@]} # 所有元素
length=${#array_name[@]} # 取得数组元素的个数
length=${#array_name[*]}
lengthn=${#array_name[1]} # 取得数组单个元素的长度
    
echo -e "OK \n" # -e 转义 \n 换行
echo -e "OK \c" # \c 不换行

# 日期
echo `date`
    
###########################################################################
###### 运算
###########################################################################
:<<EOF
    运算符：表达式和运算符之间要有空格
    关系运算符：-eq -ne -gt -lt -ge -le
    布尔运算：-a与 -o或 !非
    逻辑运算：&& || 双中括号
    字符串运算符：= != -z长度是否为0 -n长度是否不为0 $检测空
    文件测试运算符：
        -b file 	检测文件是否是块设备文件，如果是，则返回 true。 	[ -b $file ] 返回 false。
        -c file 	检测文件是否是字符设备文件，如果是，则返回 true。 	[ -c $file ] 返回 false。
        -d file 	检测文件是否是目录，如果是，则返回 true。 	[ -d $file ] 返回 false。
        -f file 	检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 	[ -f $file ] 返回 true。
        -g file 	检测文件是否设置了 SGID 位，如果是，则返回 true。 	[ -g $file ] 返回 false。
        -k file 	检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。 	[ -k $file ] 返回 false。
        -p file 	检测文件是否是有名管道，如果是，则返回 true。 	[ -p $file ] 返回 false。
        -u file 	检测文件是否设置了 SUID 位，如果是，则返回 true。 	[ -u $file ] 返回 false。
        -r file 	检测文件是否可读，如果是，则返回 true。 	[ -r $file ] 返回 true。
        -w file 	检测文件是否可写，如果是，则返回 true。 	[ -w $file ] 返回 true。
        -x file 	检测文件是否可执行，如果是，则返回 true。 	[ -x $file ] 返回 true。
        -s file 	检测文件是否为空（文件大小是否大于0），不为空返回 true。 	[ -s $file ] 返回 true。
        -e file 	检测文件（包括目录）是否存在，如果是，则返回 true。 	[ -e $file ] 返回 true。
        -S: 判断某文件是否 socket。
        -L: 检测文件是否存在并且是一个符号链接。 
EOF
###########################################################################
    
val=`expr 2 + 2`
echo "2+2=$val"

a=10
b=20
    
val=`expr $a + $b`
echo "a + b : $val"
echo "a + b : $(($a + $b))" 
val=`expr $a \* $b` # 乘号(*)前边必须加反斜杠(\)才能实现乘法运算；
echo "a * b : $val"
if [ $a == $b ] # !=  
then
   echo "a 等于 b"
fi
if [[ $a -lt 100 && $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi 

file=$0
if [ -r $file ]
then
   echo "文件可读"
else
   echo "文件不可读"
fi
if [ -w $file ]
then
   echo "文件可写"
else
   echo "文件不可写"
fi
if [ -x $file ]
then
   echo "文件可执行"
else
   echo "文件不可执行"
fi
if [ -f $file ]
then
   echo "文件为普通文件"
else
   echo "文件为特殊文件"
fi
if [ -d $file ]
then
   echo "文件是个目录"
else
   echo "文件不是个目录"
fi
if [ -s $file ]
then
   echo "文件不为空"
else
   echo "文件为空"
fi
if [ -e $file ]
then
   echo "文件存在"
else
   echo "文件不存在"
fi
    
###########################################################################
###### 定向
###########################################################################
:<<EOF
    输出重定向：
        > 覆盖重定向
        >> 追加重定向
        2> 错误覆盖重定向
        2>> 错误追加重定向
        &> 全部重定向
EOF
###########################################################################
echo "It is a test" > result.log
    
###########################################################################
###### printf命令
###########################################################################
:<<EOF
    printf format-string [arguments...]
    单引号与双引号效果一样
    格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
    如果没有 arguments，那么 %s 用NULL代替，%d 用 0 代替
    echo自动添加换行符
    %s %c %d %f都是格式替代符
    %-10s 指一个宽度为10个字符（-表示左对齐，没有则表示右对齐）
EOF
###########################################################################
printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234 
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543 
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876 
