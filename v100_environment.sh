cd ~/netdrive/Workspace/CenterFusion_official
unzip centerfusionv100.zip -d ~/runtime/conda/envs/
sudo apt-get install ffmpeg libsm6 libxext6  -y
git config --global --add safe.directory /nfs/Workspace/CenterFusion_official
source ~/runtime/conda/etc/profile.d/conda.sh
conda activate centerfusion