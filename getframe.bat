@echo OFF
chcp 1251

set VCF_FILE=gf.vcf
set WORKFILE=%~1
set FRAMETIME=%~2
set SHOT_NUM=%~3

echo>> %VCF_FILE% VirtualDub.Open("%WORKFILE%", 0, 0);
echo>> %VCF_FILE% VirtualDub.video.filters.Clear();
echo>> %VCF_FILE% VirtualDub.audio.filters.Clear();
echo>> %VCF_FILE% VirtualDub.subset.Clear();
echo>> %VCF_FILE% VirtualDub.subset.AddFrame(%FRAMETIME% * VirtualDub.video.GetFrameRate(3)/VirtualDub.video.GetFrameRate(4), 1);
echo>> %VCF_FILE% VirtualDub.SaveImageSequence("D:\\viu\\ss", ".png", 0, 0x0101);
echo>> %VCF_FILE% VirtualDub.Close();

start "" /MIN /WAIT "D:\Progs\VirtualDubMod_1_5_10_2_All_inclusive\VirtualDubMod.exe" /s"D:\viu\%VCF_FILE%" /x
move D:\viu\ss0.png D:\viu\screenshots\ss%SHOT_NUM%.png
png2jpg.exe screenshots\ss%SHOT_NUM%.png -E

del %VCF_FILE%