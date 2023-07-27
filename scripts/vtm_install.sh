cd $1
git clone https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM.git
cd VVCSoftware_VTM 
git checkout VTM-14.0
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release

