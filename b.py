hello world
 git push -u origin master：首次推送提交到远程仓库，之后就可以直接使用 git push 命令推送

     git remote -v：查看本地仓库关联的远端

     git remote set-url origin git@github.com:Username/test.git：修改关联的远端仓库网址

     git remote rm origin：删除本地仓库与远端的关联

③ git status：查看全部区域状态

     git add file：添加工作区的文件修改到缓存区 / 暂存区

     git add A/*：添加工作区 A 文件夹内的全部修改到缓存区

     git add .：添加全部修改到缓存区 / 暂存区

     git diff --cached：查看已添加到缓存区的修改

     git diff：查看未添加到缓存区的修改（不包含未被跟踪的文件，即未使用过 git add 添加到缓存区的文件）

     git checkout -- file：撤销此文件未添加到缓存区的修改（对未被跟踪的文件无效）

     git checkout .：撤销全部未添加到缓存区的修改（对未被跟踪的文件无效）

     git rm --cached file：撤销已添加到缓存区的修改

     git reset -- file：撤销已添加到缓存区的修改

     git reset --：撤销缓存区的全部内容

     git commit -m '备注'：提交缓存区的修改到本地代码库
