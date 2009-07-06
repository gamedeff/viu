@echo OFF

set VCF_FILE=gfn.vcf
set OUT_FILE=gfn.txt
set WORKFILE=%~1

echo>> %VCF_FILE% VirtualDub.Open("%WORKFILE%", 0, 0);
echo>> %VCF_FILE% Sylia.dprint(VirtualDub.video.GetRange(2));
echo>> %VCF_FILE% VirtualDub.subset.Clear();
echo>> %VCF_FILE% VirtualDub.Close();

"D:\Progs\VirtualDubMod_1_5_10_2_All_inclusive\VirtualDubMod.exe" /s"D:\viu\%VCF_FILE%" /x >%OUT_FILE%

for /f "usebackq delims=" %%i in (%OUT_FILE%) do echo %%i

del %VCF_FILE%
del %OUT_FILE%