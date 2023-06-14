cd ~/netdrive/Workspace/CenterFusion_official
unzip centerfusion1080.zip -d ~/runtime/conda/envs/
sudo apt-get install ffmpeg libsm6 libxext6  -y
cd ~/netdrive/Workspace/CenterFusion_official/DCNv2/
source ~/runtime/conda/etc/profile.d/conda.sh
conda activate centerfusion
python3 setup.py develop
cd ~/netdrive/Workspace/CenterFusion_official
git config --global --add safe.directory /nfs/Workspace/CenterFusion_official