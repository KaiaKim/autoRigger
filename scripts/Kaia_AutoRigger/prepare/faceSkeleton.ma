//Maya ASCII 2022 scene
//Name: faceSkeleton.ma
//Last modified: Fri, Sep 16, 2022 09:08:09 PM
//Codeset: 949
requires maya "2022";
requires -nodeType "colorMath" "lookdevKit" "1.0";
requires -nodeType "RedshiftOptions" -nodeType "RedshiftPostEffects" "redshift4maya" "3.0.64";
requires "stereoCamera" "10.0";
requires "mtoa" "5.0.0.4";
requires -nodeType "renderSetup" "renderSetup.py" "1.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2022";
fileInfo "version" "2022";
fileInfo "cutIdentifier" "202205171752-c25c06f306";
fileInfo "osv" "Windows 10 Home v2009 (Build: 19043)";
fileInfo "UUID" "DF1CAEE7-481F-E8CC-249A-959C0B92D0A1";
createNode transform -s -n "persp";
	rename -uid "D82E65E5-4C47-4946-6543-25BE34AAF9C2";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 2.3246262207374135 104.48857062398532 35.635699889234289 ;
	setAttr ".r" -type "double3" -7.5383527154566163 -1083.3999999997372 -2.489189747178129e-17 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "0365293B-445B-290E-367B-818C1EBDE253";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 30.149155846823;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -1.2691780924797058 100.13399887084961 6.0743212699890137 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "FFF62337-4393-2074-5FF2-D88ABB002049";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1.1745716909353294 1000.1 7.4869001705365346 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "C0950844-4EEC-C97D-4B8B-1FBF640AC18D";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 11.721212121212131;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "434DD449-4732-4527-4E6C-6FA53E007158";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1.039010376402997 103.34457844395145 1005.3469055179482 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "F0E50BEB-4AD2-46BE-B326-CD9EE02E2569";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 998.6592576984292;
	setAttr ".ow" 19.50738640824202;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" -1.6373145580291748 102.22294616699219 6.687647819519043 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "47A3963D-49E7-E493-F56B-808DC0E1818A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1004.4490180503692 103.93302690799997 8.0715578273548036 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "E85AEC9E-45B7-E51F-E66F-59BA64CE49C4";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1004.4490180503692;
	setAttr ".ow" 2.7741712179884979;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 0 100.26002307235117 4.2272380918416506 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "face_GUIDE_Grp";
	rename -uid "C28619B0-4898-324C-E99D-7AAD6712F097";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode joint -n "face_guide" -p "face_GUIDE_Grp";
	rename -uid "24A293BD-4EB6-FD8C-EA7C-F4B10CA825A9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 3.3019790515124298e-14 100 0 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3019790515124298e-14 139.54475402832031 -2 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_bind";
	setAttr ".radi" 0.3;
	setAttr ".liw" yes;
createNode joint -n "face_upper_guide" -p "face_guide";
	rename -uid "7EEC5493-451D-FE98-662D-85A5DC290B90";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -3.1029095486420873e-14 -0.1508558961503752 0.3 ;
	setAttr -l on ".tx";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1.0000000000000002 0 7.1309187385013778e-19 141.53578757853617 -1.7 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_upper_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "eye_socket_l_guide" -p "face_upper_guide";
	rename -uid "DBD54292-42DB-A1A4-AC39-A99BC5996706";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.6800000667572021 144.65299987792969 1.9069999456405642 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye_socket";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "eye_l_guide" -p "eye_socket_l_guide";
	rename -uid "D9B192CA-4098-B4F2-503E-F59A79D5848B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.6800000667572035 144.65299987792966 1.9069999456405637 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
	setAttr ".radi" 0.2;
createNode joint -n "eye_socket_r_guide" -p "face_upper_guide";
	rename -uid "F70CDEEB-4795-76E9-6D9A-B5A5BC3507AF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -2.8499724750393103 2.4711015923378596 5.2508923218665879 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 0 -1.2246467991473532e-16 0 0 1 0 0 1.2246467991473532e-16 0 -1 0
		 -3.6800000667572021 144.65299987792969 1.9069999456405642 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye_socket";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "eye_r_guide" -p "eye_socket_r_guide";
	rename -uid "56E55749-4CE5-940B-208F-C083F8151514";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 2.4492935982947064e-16 0 0 1 0 0 -2.4492935982947064e-16 0 1 0
		 -3.6800000667571995 144.65299987792969 1.9069999456405644 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
	setAttr ".radi" 0.2;
createNode joint -n "nose_bridge_guide" -p "face_upper_guide";
	rename -uid "E5D912E0-4F93-B464-EE7C-AD84ABD54774";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 2 7 ;
	setAttr -l on ".tx";
	setAttr ".r" -type "double3" -25 0 0 ;
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99996192306476117 0.0078949694251991553 -0.0037177786916076381 0
		 -0.00872653543077671 0.9046738962540336 -0.42601524505106786 0 -2.1684043449710093e-19 0.42603146702364741 0.90470834477508766 0
		 -0.019507717542005941 143.86306330870656 7.8343620802521761 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nose_brige_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "nose_guide" -p "nose_bridge_guide";
	rename -uid "4088FC3D-4DEE-2A0C-7519-DBA5CA32B4E3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 -1.5 0 ;
	setAttr -l on ".tx";
	setAttr ".r" -type "double3" 20 0 0 ;
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -6.9388939039072284e-18 4.3368086899420177e-18 0
		 6.8533465540116807e-18 0.99940289822345529 -0.034552091435368637 0 -3.6686991162046965e-18 0.034552091435368693 0.99940289822345529 0
		 -5.2041704279304213e-16 141.93141255994448 8.9694147686645316 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nose_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "sneer_l_guide" -p "nose_guide";
	rename -uid "62405AB9-40C6-A357-2CD2-9F9023137D89";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.20000000298023224 2.8421709430404007e-14 3.5527136788005009e-15 ;
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".ry";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 -6.9388939039072284e-18 4.3368086899420177e-18 0
		 7.5896831226623083e-18 0.95289882536415571 -0.30328835885937405 0 -1.6806017649044133e-18 0.30328835885937411 0.95289882536415571 0
		 0.21903214560501705 141.93141255994448 8.969414768664528 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "sneer";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "nostril_l_guide" -p "sneer_l_guide";
	rename -uid "9CF9C637-46B0-2328-DC34-83A18836E652";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on ".tx";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.97635641039468091 0.20598525391636685 -0.065560926245923301 0
		 -0.21616697222566983 0.93036887660185497 -0.29611753337043228 0 -1.6806017649044133e-18 0.30328835885937411 0.95289882536415571 0
		 0.49003214560504404 141.17998936799685 9.4803797250003345 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nostril";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "sneer_r_guide" -p "nose_guide";
	rename -uid "2FFFDA64-4EA6-8ACC-5E40-21AA0107547D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -0.2 2.8421709430404007e-14 3.5527136788005009e-15 ;
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr ".r" -type "double3" 0 0 -20 ;
	setAttr -l on ".ry";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 2.7074830858901341e-18 -1.2672836472673628e-16 0
		 4.0677231322670454e-17 0.95289953436686914 -0.30328613124144665 0 1.1959080448209269e-16 -0.30328613124144671 -0.95289953436686925 0
		 -0.2190319999999962 141.93111672133057 8.9693909197842583 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "sneer";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "nostril_r_guide" -p "sneer_r_guide";
	rename -uid "1C99F81D-48C8-8836-3D1C-059F49CE3838";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 0 -1 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.97635641039468091 0.20598540717933672 -0.065560444708500781 0
		 0.21616697222566986 0.93036956884119926 -0.29611535842138892 0 1.1959080448209269e-16 -0.30328613124144671 -0.95289953436686925 0
		 -0.49003200000001745 141.1796923348885 9.480354119496571 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nostril";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_r_guide" -p "face_upper_guide";
	rename -uid "1C30DF08-4BCA-964E-97A3-A08D184AF15E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.4146180152893066 4.0503157350175627 6.7629809498786901 ;
	setAttr ".r" -type "double3" 0 -17.00000000000006 0 ;
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_peak_r_guide" -p "brow_r_guide";
	rename -uid "9F56C765-4AD5-D6E7-2C1C-DCA494A7A0F1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 1.4215945517698256 0.4014892578125 0.31068968998799384 ;
	setAttr ".r" -type "double3" 0 -8.0000000000000551 0 ;
	setAttr -l on ".rx";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_peak";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_inner_r_guide" -p "brow_r_guide";
	rename -uid "879743D1-448F-4474-8F58-8E9F573C4320";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 3.5580569057404188 0.1350860595703125 0.075983850791793373 ;
	setAttr ".r" -type "double3" 0 17.000000000000011 0 ;
	setAttr -l on ".rx";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 0 0
		 0 0 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_inner";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_corrugator_r_guide" -p "brow_inner_r_guide";
	rename -uid "24C80431-4610-C06C-9864-7FB51D87D49D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -0.58711922168731689 0.4221038818359375 0.048930168151857245 ;
	setAttr ".r" -type "double3" 0 0 14.999999999999998 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -9.5416640443905503e-15 0 ;
	setAttr ".bps" -type "matrix" -0.96592582628906831 -0.25881904510252052 -1.2246467991473532e-16 0
		 -0.25881904510252052 0.96592582628906842 3.0814879110195774e-33 0 1.1829179713786698e-16 3.1696191514317612e-17 -1 0
		 -3.1426379680633545 147.62466326971466 8.3068027496337891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_corrugator";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_l_guide" -p "face_upper_guide";
	rename -uid "B10347F2-4F95-5321-65D2-39973B95D28D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_peak_l_guide" -p "brow_l_guide";
	rename -uid "1E3BAA3D-447E-39E2-6FF3-45BB96351BB1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on ".rx";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_peak";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_inner_l_guide" -p "brow_l_guide";
	rename -uid "E0AFC1F0-441C-CA5B-2274-A49C4EB139D0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on ".rx";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 0 0
		 0 0 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_inner";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_corrugator_l_guide" -p "brow_inner_l_guide";
	rename -uid "BAA19FF8-4FCE-BDF5-A507-77A068462336";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.96592582628906831 -0.25881904510252052 -1.2246467991473532e-16 0
		 -0.25881904510252052 0.96592582628906842 3.0814879110195774e-33 0 1.1829179713786698e-16 3.1696191514317612e-17 -1 0
		 -3.1426379680633545 147.62466326971466 8.3068027496337891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_corrugator";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "face_lower_guide" -p "face_guide";
	rename -uid "F254691B-4073-5A62-D871-8685EF384D48";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 1.2348983868225787 0.23811262572524838 ;
	setAttr -l on ".tx";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 142.92154186150913 -1.7 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_lower_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "jaw_trans_guide" -p "face_lower_guide";
	rename -uid "9F922C50-4868-3C8D-9C5A-9291AFB1725B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 -1.6262223533614701 -0.37528104248188243 ;
	setAttr -l on ".tx";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 141.29531950814766 -0.89218694903278761 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "jaw_trans_bind";
	setAttr ".radi" 0.2;
createNode joint -n "jaw_guide" -p "jaw_trans_guide";
	rename -uid "988CF44A-4F9A-D032-0998-76980C3EF764";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 1.4210854715202004e-14 7.5495165674510645e-15 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr ".r" -type "double3" 14.999999999999998 0 0 ;
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "zyx";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96126169593831889 0.27563735581699911 0
		 0 -0.27563735581699911 0.96126169593831889 0 0 141.29531950814768 -0.89218694903278006 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "jaw_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "jaw_tip_guide" -p "jaw_guide";
	rename -uid "3FD8F5D5-4ED4-E8BB-F541-58843000CAF8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 0 5 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.98052129010354039 0.19641282965653953 0
		 0 -0.19641282965653953 0.98052129010354039 0 0 146.72480613686366 6.7018096387646464 1;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_01_guide" -p "face_GUIDE_Grp";
	rename -uid "6A05D2E8-41F4-77B2-4E76-A687AE71B871";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 1.9899819368295736e-15 97.098712879469261 3.4761210207375486 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.577674211802957 -64.581845045189851 89.618554356893895 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_02_guide" -p "tongue_01_guide";
	rename -uid "B2D45A57-4256-2018-5ECF-1FA913EF5163";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.6124703227624384 4.4130449852155439e-15 4.9971018038693095e-18 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.043325316350068269 -0.18838287833144121 -12.46555523627443 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_03_guide" -p "tongue_02_guide";
	rename -uid "86932918-4202-61BE-F78F-EF9A1E493E10";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.65907319232506711 7.5447105058028003e-15 -3.4452835548585984e-18 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.00014551855653038924 0.002556308020765508 -6.5161244795551916 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_04_guide" -p "tongue_03_guide";
	rename -uid "22561F32-4F17-7263-C104-698E1FA9AF34";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.63449551202333865 2.5291854570178403e-15 -4.6430142797957764e-19 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.98775210804452e-05 -0.0020099932944911691 -3.4126630577571069 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_05_guide" -p "tongue_04_guide";
	rename -uid "35E6DADA-4957-1049-6FF8-9C860F6E1B9B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.5874599140357244 -1.977606734958324e-14 7.9614261368980907e-19 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.00035490689171974497 0.014237736791363096 -2.662717444288174 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_06_guide" -p "tongue_05_guide";
	rename -uid "580E0010-488A-EC8C-22CF-2EB53DDDE499";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.43079789301606392 -4.1111102757965079e-15 -7.9674311689481953e-18 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.0012898873536458767 0.018933565599269068 -4.2577920543636401 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_07_guide" -p "tongue_06_guide";
	rename -uid "EAF32DD7-4D35-8E4F-E4E0-41BE656A700D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.38893662555992586 -8.7487573996369602e-15 -2.4104781835788241e-18 ;
	setAttr ".r" -type "double3" 6.1224124612957134e-14 2.4425666030301852e-14 0 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".radi" 0.2;
createNode joint -n "teeth_upper_guide" -p "face_GUIDE_Grp";
	rename -uid "61F70567-421F-2B9C-5682-64BC75C1C817";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.013299210928382481 98.386172208167125 6.5562535820716867 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".is" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.98052129010354039 0.19641282965653928 0
		 0 -0.19641282965653928 0.98052129010354039 0 0.013299210928380489 138.11293712846211 7.0540576876644634 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "teeth_upper_bind";
	setAttr ".radi" 0.2;
createNode joint -n "teeth_lower_guide" -p "face_GUIDE_Grp";
	rename -uid "3336476B-4B77-E34A-58B8-08B328BF0081";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 1.989981936829574e-15 96.993590202620823 5.3547644030562918 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 6.5376777919745077 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.9805212901035405 0.19641282965653939 0
		 0 -0.19641282965653939 0.9805212901035405 0 0.013299211103944053 138.10891582416616 7.2178271315535767 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "teeth_lower_bind";
	setAttr ".radi" 0.2;
createNode transform -n "lid_upper_r_guideCrv" -p "face_GUIDE_Grp";
	rename -uid "454F0F10-45FA-BB60-C86F-A0BE72B6841D";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
createNode nurbsCurve -n "lid_upper_r_guideCrvShape" -p "lid_upper_r_guideCrv";
	rename -uid "5BD26841-417A-6D30-CD9D-DE8E192AF816";
	setAttr -k off ".v";
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "lid_upper_r_guideCrvShapeOrig" -p "lid_upper_r_guideCrv";
	rename -uid "3F05ECAC-4715-2686-2F96-879F0AAD7C7C";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 11 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster2";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster3";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster4";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster5";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster2_1";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster3_1";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster4_1";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster5_1";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster6";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".cc" -type "nurbsCurve" 
		2 3 0 no 3
		6 0 0 0.33333333333333337 0.66666666666666674 1 1
		5
		-1.6306558404308684 101.9526128673328 6.0392417907714844
		-1.8873145991642415 102.70483066528182 6.4376478179797871
		-3.0241072214444942 103.14755964870648 6.5843792242413191
		-3.9834420987961319 102.85642513926248 6.0141117327555849
		-4.2763590812683105 102.36575814485055 5.4278616905212402
		

		"gtag" 11
		"cluster1" 1 "cv[0]"
		"cluster1_1" 1 "cv[0]"
		"cluster2" 1 "cv[1]"
		"cluster2_1" 1 "cv[0]"
		"cluster3" 1 "cv[2]"
		"cluster3_1" 1 "cv[4]"
		"cluster4" 1 "cv[3]"
		"cluster4_1" 1 "cv[1]"
		"cluster5" 1 "cv[4]"
		"cluster5_1" 1 "cv[2]"
		"cluster6" 1 "cv[3]";
createNode transform -n "lid_lower_r_guideCrv" -p "face_GUIDE_Grp";
	rename -uid "BD02F64B-4C3B-1A04-41DB-F8B7B4C1858B";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
createNode nurbsCurve -n "lid_lower_r_guideCrvShape" -p "lid_lower_r_guideCrv";
	rename -uid "C4736B16-4BBF-7A0A-89A8-6F8AC0BBDB41";
	setAttr -k off ".v";
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "lid_lower_r_guideCrvShapeOrig" -p "lid_lower_r_guideCrv";
	rename -uid "54005F47-4A44-E633-2B41-CD84D7A5747E";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 11 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster20";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster21";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster22";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster23";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster24";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster2";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster3";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster10";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster11";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster12";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".cc" -type "nurbsCurve" 
		2 3 0 no 3
		6 0 0 0.33333333333333337 0.66666666666666674 1 1
		5
		-1.6306558404308684 101.9526128673328 6.0392417907714844
		-2.2685830173039618 101.83709244633017 6.2494789684471135
		-3.1095689168870786 101.70172134613753 6.2902151540887123
		-4.0393744896243549 101.97178108066886 5.8298720770307177
		-4.2763590812683105 102.36575814485055 5.4278616905212402
		

		"gtag" 11
		"cluster1" 1 "cv[0]"
		"cluster10" 1 "cv[3]"
		"cluster11" 1 "cv[2]"
		"cluster12" 1 "cv[1]"
		"cluster2" 1 "cv[0]"
		"cluster20" 1 "cv[0]"
		"cluster21" 1 "cv[1]"
		"cluster22" 1 "cv[2]"
		"cluster23" 1 "cv[3]"
		"cluster24" 1 "cv[4]"
		"cluster3" 1 "cv[4]";
createNode transform -n "lid_mid_r_guideCrv" -p "face_GUIDE_Grp";
	rename -uid "402FCF76-4FAE-9A30-27EF-28989A853486";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
createNode nurbsCurve -n "lid_mid_r_guideCrvShape" -p "lid_mid_r_guideCrv";
	rename -uid "28EFE40D-41E2-DE9E-186A-13A575615751";
	setAttr -k off ".v";
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "lid_mid_r_guideCrvShapeOrig" -p "lid_mid_r_guideCrv";
	rename -uid "7D941D12-43CF-CC4B-1A17-CA952D55E2AB";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".ovc" 13;
	setAttr -s 5 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster2";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster3";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster4";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster5";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".cc" -type "nurbsCurve" 
		2 3 0 no 3
		6 0 0 0.33333333333333337 0.66666666666666674 1 1
		5
		-2.870902080215247 143.40175017140305 6.8712303854058892
		-2.927262794060709 145.12279187167218 6.8171169149639654
		-4.9873711608169913 145.96410022162803 6.8130764932122876
		-6.9050312399413762 145.01827467771685 5.8165655596147765
		-6.983070167784529 143.83236694335938 5.5843982696533203
		

		"gtag" 5
		"cluster1" 1 "cv[0]"
		"cluster2" 1 "cv[1]"
		"cluster3" 1 "cv[2]"
		"cluster4" 1 "cv[3]"
		"cluster5" 1 "cv[4]";
createNode nurbsCurve -n "lid_mid_r_guideCrvShapeOrig1" -p "lid_mid_r_guideCrv";
	rename -uid "71F2817E-49D6-AFF1-0A3C-008FD9A7BD5A";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 6 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster2";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster3";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster7";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster8";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster9";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".cc" -type "nurbsCurve" 
		2 3 0 no 3
		6 0 0 0.33333333333333337 0.66666666666666674 1 1
		5
		-1.6306558404308684 101.9526128673328 6.0392417907714844
		-1.8873145991642415 101.9729465735993 6.4376478179797871
		-3.0820012692224812 102.08850038288118 6.5843792242413191
		-4.0413361465741175 102.23382366637006 6.0141117327555849
		-4.2763590812683105 102.36575814485055 5.4278616905212402
		

		"gtag" 6
		"cluster1" 1 "cv[0]"
		"cluster2" 1 "cv[0]"
		"cluster3" 1 "cv[4]"
		"cluster7" 1 "cv[2]"
		"cluster8" 1 "cv[1]"
		"cluster9" 1 "cv[3]";
createNode transform -n "lip_upper_guideCrv" -p "face_GUIDE_Grp";
	rename -uid "77AA4A07-43D6-90DD-662B-7D93AE3C8C4B";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
createNode nurbsCurve -n "lip_upper_guideCrvShape" -p "lip_upper_guideCrv";
	rename -uid "D3E14AD8-476E-4EE2-BFD8-35A6E0248FFB";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_upper_guideCrvShapeOrig" -p "lip_upper_guideCrv";
	rename -uid "1679B4E0-4154-8D60-DCDF-24BE06A117FA";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 35 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster14";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster15";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster16";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster17";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster18";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13_1";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster14_1";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster15_1";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster16_1";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster17_1";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster18_1";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster19_1";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.3085188921679967 97.72339631953372 6.1240477956834445
		-0.76369939659500408 97.875628709476885 6.4950139526250359
		1.670394704933599e-19 97.929771954570768 6.7207808961601136
		0.76369939659500408 97.875628709476885 6.4950139526250359
		1.3085188921679967 97.72339631953372 6.1240477956834445
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 35
		"cluster1" 1 "cv[0]"
		"cluster13" 1 "cv[0]"
		"cluster13_1" 1 "cv[0]"
		"cluster14" 1 "cv[1]"
		"cluster14_1" 1 "cv[1]"
		"cluster15" 1 "cv[2]"
		"cluster15_1" 1 "cv[2]"
		"cluster16" 1 "cv[3]"
		"cluster16_1" 1 "cv[3]"
		"cluster17" 1 "cv[4]"
		"cluster17_1" 1 "cv[4]"
		"cluster18" 1 "cv[5]"
		"cluster18_1" 1 "cv[5]"
		"cluster19" 1 "cv[6]"
		"cluster19_1" 1 "cv[6]"
		"cluster1_1" 1 "cv[1]"
		"cluster1_10" 1 "cv[3]"
		"cluster1_11" 1 "cv[4]"
		"cluster1_12" 1 "cv[5]"
		"cluster1_13" 1 "cv[6]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[1]"
		"cluster1_16" 1 "cv[2]"
		"cluster1_17" 1 "cv[3]"
		"cluster1_18" 1 "cv[4]"
		"cluster1_19" 1 "cv[5]"
		"cluster1_2" 1 "cv[2]"
		"cluster1_20" 1 "cv[6]"
		"cluster1_3" 1 "cv[3]"
		"cluster1_4" 1 "cv[4]"
		"cluster1_5" 1 "cv[5]"
		"cluster1_6" 1 "cv[6]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[1]"
		"cluster1_9" 1 "cv[2]";
createNode transform -n "lip_lower_guideCrv" -p "face_GUIDE_Grp";
	rename -uid "411261A9-4209-941B-C4BF-ABB2C02CDC43";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
createNode nurbsCurve -n "lip_lower_guideCrvShape" -p "lip_lower_guideCrv";
	rename -uid "E223D75F-4B36-690D-0669-95919B446B5F";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_lower_guideCrvShapeOrig" -p "lip_lower_guideCrv";
	rename -uid "CCDD2281-4A8A-0CA1-EAB0-4595B6B96B2A";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 36 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster10";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster11";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster12";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster20";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster21";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster22";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster23";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster24";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[35].gtagnm" -type "string" "cluster26";
	setAttr ".gtag[35].gtagcmp" -type "componentList" 2 "cv[0:2]" "cv[4:6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.2576395445478417 97.402661377988451 6.024359840771357
		-0.73120154860842312 97.235717429291398 6.2578796389602918
		3.7669309661685105e-18 97.120437438767468 6.45093567580557
		0.73120154860842312 97.235717429291398 6.2578796389602918
		1.2576395445478417 97.402661377988451 6.024359840771357
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 36
		"cluster1" 1 "cv[0]"
		"cluster10" 1 "cv[4]"
		"cluster11" 1 "cv[5]"
		"cluster12" 1 "cv[6]"
		"cluster13" 1 "cv[0]"
		"cluster19" 1 "cv[6]"
		"cluster1_1" 1 "cv[6]"
		"cluster1_10" 1 "cv[4]"
		"cluster1_11" 1 "cv[3]"
		"cluster1_12" 1 "cv[2]"
		"cluster1_13" 1 "cv[1]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[6]"
		"cluster1_16" 1 "cv[5]"
		"cluster1_17" 1 "cv[4]"
		"cluster1_18" 1 "cv[3]"
		"cluster1_19" 1 "cv[2]"
		"cluster1_2" 1 "cv[5]"
		"cluster1_20" 1 "cv[1]"
		"cluster1_3" 1 "cv[4]"
		"cluster1_4" 1 "cv[3]"
		"cluster1_5" 1 "cv[2]"
		"cluster1_6" 1 "cv[1]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[6]"
		"cluster1_9" 1 "cv[5]"
		"cluster20" 1 "cv[5]"
		"cluster21" 1 "cv[4]"
		"cluster22" 1 "cv[3]"
		"cluster23" 1 "cv[2]"
		"cluster24" 1 "cv[1]"
		"cluster26" 2 "cv[0:2]" "cv[4:6]"
		"cluster6" 1 "cv[0]"
		"cluster7" 1 "cv[1]"
		"cluster8" 1 "cv[2]"
		"cluster9" 1 "cv[3]";
createNode transform -n "cls_Grp" -p "face_GUIDE_Grp";
	rename -uid "F9A25F34-4E23-E792-239E-539F2D256A8A";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode transform -n "lid_handle_00" -p "cls_Grp";
	rename -uid "EC36786B-4EFB-838E-20AF-0ABA68BD50ED";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -1.6306558847427368 101.95261383056641 6.0392417907714844 ;
	setAttr ".sp" -type "double3" -1.6306558847427368 101.95261383056641 6.0392417907714844 ;
createNode clusterHandle -n "lid_handle_00Shape" -p "lid_handle_00";
	rename -uid "29D31C95-4BD3-F631-E44A-97B1BE5C5350";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.6306558847427368 101.95261383056641 6.0392417907714844 ;
createNode transform -n "lid_handle_07" -p "cls_Grp";
	rename -uid "011654E6-4A2E-87D0-3A1A-EC8E41B1C8E0";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -4.2763590812683105 102.36576080322266 5.4278616905212402 ;
	setAttr ".sp" -type "double3" -4.2763590812683105 102.36576080322266 5.4278616905212402 ;
createNode clusterHandle -n "lid_handle_07Shape" -p "lid_handle_07";
	rename -uid "652F90E0-458A-C7FE-A90A-D789D9EDC249";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -4.2763590812683105 102.36576080322266 5.4278616905212402 ;
createNode transform -n "lid_handle_01" -p "cls_Grp";
	rename -uid "72AF31DA-4366-89ED-B31D-DBB56CFDDC5C";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -1.8873145580291748 102.704833984375 6.437647819519043 ;
	setAttr ".sp" -type "double3" -1.8873145580291748 102.704833984375 6.437647819519043 ;
createNode clusterHandle -n "lid_handle_01Shape" -p "lid_handle_01";
	rename -uid "25F4694C-48A6-E731-1FD1-26BD9ABFCF31";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.8873145580291748 102.704833984375 6.437647819519043 ;
createNode transform -n "lid_handle_02" -p "cls_Grp";
	rename -uid "14DBBA12-4541-8588-6F94-448BCF3715C9";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -3.0241072177886963 103.14756011962891 6.5843791961669922 ;
	setAttr ".sp" -type "double3" -3.0241072177886963 103.14756011962891 6.5843791961669922 ;
createNode clusterHandle -n "lid_handle_02Shape" -p "lid_handle_02";
	rename -uid "02F364E0-46DA-A209-392A-E2962D488493";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -3.0241072177886963 103.14756011962891 6.5843791961669922 ;
createNode transform -n "lid_handle_03" -p "cls_Grp";
	rename -uid "EDB5F00D-42A7-1A2B-A898-21A853684AA4";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".t" -type "double3" -0.044666730188185788 0.010944227509568805 0 ;
	setAttr ".rp" -type "double3" -3.9834420680999756 102.85642242431641 6.0141115188598633 ;
	setAttr ".sp" -type "double3" -3.9834420680999756 102.85642242431641 6.0141115188598633 ;
createNode clusterHandle -n "lid_handle_03Shape" -p "lid_handle_03";
	rename -uid "8866AEA8-42EE-8608-20A9-B183BBDE544C";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -3.9834420680999756 102.85642242431641 6.0141115188598633 ;
createNode transform -n "lid_handle_09" -p "cls_Grp";
	rename -uid "D365971B-4288-7335-ADD9-AF9713398DEF";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".t" -type "double3" -0.028870679947575972 0.21103985045643014 0 ;
	setAttr ".rp" -type "double3" -3.0820012092590332 102.0885009765625 6.5843791961669922 ;
	setAttr ".sp" -type "double3" -3.0820012092590332 102.0885009765625 6.5843791961669922 ;
createNode clusterHandle -n "lid_handle_09Shape" -p "lid_handle_09";
	rename -uid "817185E0-4958-497F-94AA-299754DE1971";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -3.0820012092590332 102.0885009765625 6.5843791961669922 ;
createNode transform -n "lid_handle_08" -p "cls_Grp";
	rename -uid "0336991E-4D81-6818-1736-AB8CBC2F2789";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".t" -type "double3" -0.30013416711655028 0.20599220846305855 0 ;
	setAttr ".rp" -type "double3" -1.8873145580291748 101.97294616699219 6.437647819519043 ;
	setAttr ".sp" -type "double3" -1.8873145580291748 101.97294616699219 6.437647819519043 ;
createNode clusterHandle -n "lid_handle_08Shape" -p "lid_handle_08";
	rename -uid "148944DA-441D-DA2D-7BD4-C4B18CBE0A31";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.8873145580291748 101.97294616699219 6.437647819519043 ;
createNode transform -n "lid_handle_10" -p "cls_Grp";
	rename -uid "24C03D69-47D6-5C8A-23C9-C19C89F4C160";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".t" -type "double3" 0.025238209966842007 0.10600048186073252 0 ;
	setAttr ".rp" -type "double3" -4.0413360595703125 102.23382568359375 6.0141115188598633 ;
	setAttr ".sp" -type "double3" -4.0413360595703125 102.23382568359375 6.0141115188598633 ;
createNode clusterHandle -n "lid_handle_10Shape" -p "lid_handle_10";
	rename -uid "B30A7537-426E-AEF5-53ED-239D7014C216";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -4.0413360595703125 102.23382568359375 6.0141115188598633 ;
createNode transform -n "lid_handle_06" -p "cls_Grp";
	rename -uid "FCE479BB-44BF-2D2D-9DC8-DE81B9B94613";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -4.0393743515014648 101.97177886962891 5.8298721313476562 ;
	setAttr ".sp" -type "double3" -4.0393743515014648 101.97177886962891 5.8298721313476562 ;
createNode clusterHandle -n "lid_handle_06Shape" -p "lid_handle_06";
	rename -uid "D32DDEA2-4AB5-CBD3-94A8-838E8284DB51";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -4.0393743515014648 101.97177886962891 5.8298721313476562 ;
createNode transform -n "lid_handle_05" -p "cls_Grp";
	rename -uid "52A9826E-43EC-B44A-800A-0FAEB95BFA6A";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -3.1095688343048096 101.70172119140625 6.290215015411377 ;
	setAttr ".sp" -type "double3" -3.1095688343048096 101.70172119140625 6.290215015411377 ;
createNode clusterHandle -n "lid_handle_05Shape" -p "lid_handle_05";
	rename -uid "C20EE068-4651-7A8A-866A-C2B74269EC4B";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -3.1095688343048096 101.70172119140625 6.290215015411377 ;
createNode transform -n "lid_handle_04" -p "cls_Grp";
	rename -uid "403536E3-44A3-455D-B605-ADB2D665079D";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".t" -type "double3" 0.042164199092656229 -0.0711520859688477 0 ;
	setAttr ".rp" -type "double3" -2.2685830593109131 101.83708953857422 6.249478816986084 ;
	setAttr ".sp" -type "double3" -2.2685830593109131 101.83708953857422 6.249478816986084 ;
createNode clusterHandle -n "lid_handle_04Shape" -p "lid_handle_04";
	rename -uid "3CB7DEAF-4A6D-F104-87AF-96BB3C28BB4B";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -2.2685830593109131 101.83708953857422 6.249478816986084 ;
createNode transform -n "lip_handle_03" -p "cls_Grp";
	rename -uid "ED3F5690-43C1-1F3B-3246-E1B3F0607245";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -1.7380028963088989 97.562576293945312 5.7681660652160645 ;
	setAttr ".sp" -type "double3" -1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode clusterHandle -n "lip_handle_03Shape" -p "lip_handle_03";
	rename -uid "730368EF-4307-FD87-B828-B1832325A36C";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode transform -n "lip_handle_02" -p "cls_Grp";
	rename -uid "E33C6054-447D-A49F-6DAB-AC835163A92D";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -1.3085188865661621 97.723396301269531 6.1240477561950684 ;
	setAttr ".sp" -type "double3" -1.3085188865661621 97.723396301269531 6.1240477561950684 ;
createNode clusterHandle -n "lip_handle_02Shape" -p "lip_handle_02";
	rename -uid "C4656433-4CA1-5FDE-E732-B282C56B4875";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.3085188865661621 97.723396301269531 6.1240477561950684 ;
createNode transform -n "lip_handle_01" -p "cls_Grp";
	rename -uid "012C1DEA-4D09-64C1-B77C-31BEB46048E4";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -0.76369941234588623 97.875625610351562 6.4950141906738281 ;
	setAttr ".sp" -type "double3" -0.76369941234588623 97.875625610351562 6.4950141906738281 ;
createNode clusterHandle -n "lip_handle_01Shape" -p "lip_handle_01";
	rename -uid "667C184E-4E76-50AE-C23F-15AA55E9ACA1";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -0.76369941234588623 97.875625610351562 6.4950141906738281 ;
createNode transform -n "lip_handle_00" -p "cls_Grp";
	rename -uid "91DFEFC7-43DE-FF49-2F70-FFA48E6C6762";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr -l on ".tx";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 1.670394699563718e-19 97.929771423339844 6.7207808494567871 ;
	setAttr ".sp" -type "double3" 1.670394699563718e-19 97.929771423339844 6.7207808494567871 ;
createNode clusterHandle -n "lip_handle_00Shape" -p "lip_handle_00";
	rename -uid "C9FA698B-4672-A66F-CCC7-01B440869DE1";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.670394699563718e-19 97.929771423339844 6.7207808494567871 ;
createNode transform -n "lip_handle_06" -p "cls_Grp";
	rename -uid "D9E9569C-40A6-C8BC-99D9-C6AAED2D38DA";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr -l on ".tx";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 3.7669308787297348e-18 97.120437622070312 6.4509358406066895 ;
	setAttr ".sp" -type "double3" 3.7669308787297348e-18 97.120437622070312 6.4509358406066895 ;
createNode clusterHandle -n "lip_handle_06Shape" -p "lip_handle_06";
	rename -uid "443D8373-44ED-F854-0FD1-0286CD06C4DA";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 3.7669308787297348e-18 97.120437622070312 6.4509358406066895 ;
createNode transform -n "lip_handle_05" -p "cls_Grp";
	rename -uid "645420F5-4785-9BED-E381-6498DDEC6DCC";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -0.73120152950286865 97.2357177734375 6.2578797340393066 ;
	setAttr ".sp" -type "double3" -0.73120152950286865 97.2357177734375 6.2578797340393066 ;
createNode clusterHandle -n "lip_handle_05Shape" -p "lip_handle_05";
	rename -uid "61CCE918-48CE-A90F-6748-E389B6D411ED";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -0.73120152950286865 97.2357177734375 6.2578797340393066 ;
createNode transform -n "lip_handle_04" -p "cls_Grp";
	rename -uid "E2519F91-4DA8-D1EB-446D-DC8D1571A8C5";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".rp" -type "double3" -1.2576395273208618 97.402664184570312 6.0243597030639648 ;
	setAttr ".sp" -type "double3" -1.2576395273208618 97.402664184570312 6.0243597030639648 ;
createNode clusterHandle -n "lip_handle_04Shape" -p "lip_handle_04";
	rename -uid "2151DD10-4CEA-F916-F113-F8A2346973AF";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.2576395273208618 97.402664184570312 6.0243597030639648 ;
createNode transform -n "NOTOUCH" -p "face_GUIDE_Grp";
	rename -uid "C9C01244-4C6E-2868-F7AD-3DB0B63227C0";
createNode joint -n "cheek_lower_l_bind" -p "NOTOUCH";
	rename -uid "A8C64B32-4AD2-A619-BD95-8D9B02D20B18";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 4.2566351890563965 98.0987548828125 5.7940290570259094 ;
	setAttr ".r" -type "double3" -42.012001037597656 39.952312469482422 -17.685 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.7303514067889878 0.2328743016850465 -0.6421498129066523 0
		 0.18375779411905019 0.83845213017616349 0.51306052128725965 0 0.65789048914074399 -0.49271450660372867 0.56957222481472602 0
		 5.2382864952087518 136.72753906250006 5.2657613754272754 1;
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_l_bind" -p "NOTOUCH";
	rename -uid "C7A64542-457F-38DB-EBA5-999987E1FED4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 4.8409991264343262 99.732627868652344 5.706020176410675 ;
	setAttr ".r" -type "double3" -25 40 -11 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.75197004909461695 0.14616817060531687 -0.64278760968653892 0
		 0.093731058820309771 0.94149034561144773 0.3237443709670646 0 0.65249945124656084 -0.30369523378270474 0.69427204401488418 0
		 5.8340487480163423 138.73069763183588 6.3339762687682724 1;
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_upper_l_bind" -p "NOTOUCH";
	rename -uid "42A58A16-4AC4-3FB2-3F73-D6875B90214A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 4.008873462677002 100.92861938476562 6.5781286358833313 ;
	setAttr ".r" -type "double3" -10 25 -9 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.89514963424668026 0.14177777382687393 -0.42261826174069944 0
		 -0.081574497416672637 0.98416337441241075 0.15737869562426277 0 0.43823821567641935 -0.10640260952567306 0.89253893528903006 0
		 5.0194830894470224 141.20631408691403 7.2503566741943315 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_lower_r_bind" -p "NOTOUCH";
	rename -uid "564294C5-4C65-8F72-540E-70A38A1264FC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.2566351890563947 98.0987548828125 5.7940290570259094 ;
	setAttr ".r" -type "double3" 42.012 -39.952313064542345 -17.685 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.7303514067889878 0.2328743016850463 -0.64214981290665241 0
		 -0.18375779411905063 0.83845213017616316 0.51306052128725987 0 0.65789048914074377 0.49271450660372917 -0.56957222481472602 0
		 -5.3362746238708505 136.67111206054699 5.2705068588257085 1;
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_r_bind" -p "NOTOUCH";
	rename -uid "09579F77-44CE-FBA2-C7B9-F38B01B6CCBB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.8409991264343244 99.732627868652344 5.706020176410675 ;
	setAttr ".r" -type "double3" 25 -39.99999999999995 -11 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.75197004909461707 0.14616817060531706 -0.64278760968653925 0
		 -0.093731058820309424 0.94149034561144784 0.32374437096706443 0 0.65249945124656117 0.30369523378270435 -0.69427204401488463 0
		 -6.3155222335360017 139.21096395275728 6.1109353515469138 1;
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_upper_r_bind" -p "NOTOUCH";
	rename -uid "C33E2DDC-4906-6003-09D6-E3A56E168A4E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.0088734626770002 100.92861938476562 6.5781286358833313 ;
	setAttr ".r" -type "double3" 10 -25.000000000000004 -9 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.89514963424668026 0.14177777382687393 -0.42261826174069961 0
		 0.081574497416672664 0.98416337441241075 0.1573786956242626 0 0.43823821567641952 0.10640260952567288 -0.89253893528902983 0
		 -5.0194792747497514 141.20631408691409 7.2503585815429732 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_upper_r_guide" -p "NOTOUCH";
	rename -uid "905B3D1D-4FB8-24C5-CEEC-32A69D197EA1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.0088734626770002 100.92861938476562 6.5781286358833313 ;
	setAttr ".r" -type "double3" 10 -25.000000000000004 -9 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.89514963424668026 0.14177777382687393 -0.42261826174069961 0
		 0.081574497416672664 0.98416337441241075 0.1573786956242626 0 0.43823821567641952 0.10640260952567288 -0.89253893528902983 0
		 -5.0194792747497514 141.20631408691409 7.2503585815429732 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_r_guide" -p "NOTOUCH";
	rename -uid "AE0282EA-4898-8F9D-73CA-D492BDED897B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.8409991264343244 99.732627868652344 5.706020176410675 ;
	setAttr ".r" -type "double3" 25 -39.99999999999995 -11 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.75197004909461707 0.14616817060531706 -0.64278760968653925 0
		 -0.093731058820309424 0.94149034561144784 0.32374437096706443 0 0.65249945124656117 0.30369523378270435 -0.69427204401488463 0
		 -6.3155222335360017 139.21096395275728 6.1109353515469138 1;
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_lower_r_guide" -p "NOTOUCH";
	rename -uid "A22B6A19-419A-8348-4222-1FB1D5265EB5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.2566351890563947 98.0987548828125 5.7940290570259094 ;
	setAttr ".r" -type "double3" 42.012 -39.952313064542345 -17.685 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.7303514067889878 0.2328743016850463 -0.64214981290665241 0
		 -0.18375779411905063 0.83845213017616316 0.51306052128725987 0 0.65789048914074377 0.49271450660372917 -0.56957222481472602 0
		 -5.3362746238708505 136.67111206054699 5.2705068588257085 1;
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_upper_l_guide" -p "NOTOUCH";
	rename -uid "125BD0F2-4B6F-40C4-053C-87934E4B8D18";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.89514963424668026 0.14177777382687393 -0.42261826174069944 0
		 -0.081574497416672637 0.98416337441241075 0.15737869562426277 0 0.43823821567641935 -0.10640260952567306 0.89253893528903006 0
		 5.0194830894470224 141.20631408691403 7.2503566741943315 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_l_guide" -p "NOTOUCH";
	rename -uid "A09AD6A0-4A11-A638-8FD7-0BBCDBF1B44D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.75197004909461695 0.14616817060531687 -0.64278760968653892 0
		 0.093731058820309771 0.94149034561144773 0.3237443709670646 0 0.65249945124656084 -0.30369523378270474 0.69427204401488418 0
		 5.8340487480163423 138.73069763183588 6.3339762687682724 1;
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "cheek_lower_l_guide" -p "NOTOUCH";
	rename -uid "FC9825DA-487C-A796-2045-30886E29DF8B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.7303514067889878 0.2328743016850465 -0.6421498129066523 0
		 0.18375779411905019 0.83845213017616349 0.51306052128725965 0 0.65789048914074399 -0.49271450660372867 0.56957222481472602 0
		 5.2382864952087518 136.72753906250006 5.2657613754272754 1;
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode transform -n "NOTOUCH_crv_Grp" -p "NOTOUCH";
	rename -uid "73E61AB6-42A5-9A96-8717-60B4969D80BF";
createNode transform -n "lip_lower_frown_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "2BCB9C69-4EEB-E8BE-FCA8-4A9CA8902215";
createNode nurbsCurve -n "lip_lower_frown_guideCrvShape" -p "lip_lower_frown_guideCrv";
	rename -uid "FE67902F-47CC-73D0-156E-46808220DBA4";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_lower_frown_guideCrvShapeOrig" -p "lip_lower_frown_guideCrv";
	rename -uid "380B6069-452B-8520-694E-0691F8A54C16";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 35 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster10";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster11";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster12";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster20";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster21";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster22";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster23";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster24";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.2576395445478417 97.402661377988451 6.024359840771357
		-0.73120154860842312 97.235717429291398 6.2578796389602918
		3.7669309661685105e-18 97.120437438767468 6.45093567580557
		0.73120154860842312 97.235717429291398 6.2578796389602918
		1.2576395445478417 97.402661377988451 6.024359840771357
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 35
		"cluster1" 1 "cv[0]"
		"cluster10" 1 "cv[4]"
		"cluster11" 1 "cv[5]"
		"cluster12" 1 "cv[6]"
		"cluster13" 1 "cv[0]"
		"cluster19" 1 "cv[6]"
		"cluster1_1" 1 "cv[6]"
		"cluster1_10" 1 "cv[4]"
		"cluster1_11" 1 "cv[3]"
		"cluster1_12" 1 "cv[2]"
		"cluster1_13" 1 "cv[1]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[6]"
		"cluster1_16" 1 "cv[5]"
		"cluster1_17" 1 "cv[4]"
		"cluster1_18" 1 "cv[3]"
		"cluster1_19" 1 "cv[2]"
		"cluster1_2" 1 "cv[5]"
		"cluster1_20" 1 "cv[1]"
		"cluster1_3" 1 "cv[4]"
		"cluster1_4" 1 "cv[3]"
		"cluster1_5" 1 "cv[2]"
		"cluster1_6" 1 "cv[1]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[6]"
		"cluster1_9" 1 "cv[5]"
		"cluster20" 1 "cv[5]"
		"cluster21" 1 "cv[4]"
		"cluster22" 1 "cv[3]"
		"cluster23" 1 "cv[2]"
		"cluster24" 1 "cv[1]"
		"cluster6" 1 "cv[0]"
		"cluster7" 1 "cv[1]"
		"cluster8" 1 "cv[2]"
		"cluster9" 1 "cv[3]";
createNode nurbsCurve -n "lip_lower_frown_guideCrvShapeOrig1" -p "lip_lower_frown_guideCrv";
	rename -uid "9EC71A85-45F2-5245-DC21-2D9162C64E46";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 2 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster26";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 2 "cv[0:2]" "cv[4:6]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster26_1";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 2 "cv[0:2]" "cv[4:6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028963088989 97.562576293945312 5.7681660652160645
		-1.2576395273208618 97.402664184570312 6.0243597030639648
		-0.73120152950286865 97.2357177734375 6.2578797340393066
		3.7669308787297348e-18 97.120437622070312 6.4509358406066895
		0.73120152950286865 97.2357177734375 6.2578797340393066
		1.2576395273208618 97.402664184570312 6.0243597030639648
		1.7380028963088989 97.562576293945312 5.7681660652160645
		

		"gtag" 2
		"cluster26" 2 "cv[0:2]" "cv[4:6]"
		"cluster26_1" 2 "cv[0:2]" "cv[4:6]";
createNode transform -n "lip_upper_frown_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "169D8A4D-4107-3F0C-B1B5-059C0C91F4E9";
createNode nurbsCurve -n "lip_upper_frown_guideCrvShape" -p "lip_upper_frown_guideCrv";
	rename -uid "338EFC70-4EEA-6658-4F20-B8AE73886007";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_upper_frown_guideCrvShapeOrig" -p "lip_upper_frown_guideCrv";
	rename -uid "BC34D36D-4C7C-3132-EEBB-A68CC092598E";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 35 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster14";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster15";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster16";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster17";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster18";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13_1";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster14_1";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster15_1";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster16_1";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster17_1";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster18_1";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster19_1";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.3085188921679967 97.72339631953372 6.1240477956834445
		-0.76369939659500408 97.875628709476885 6.4950139526250359
		1.670394704933599e-19 97.929771954570768 6.7207808961601136
		0.76369939659500408 97.875628709476885 6.4950139526250359
		1.3085188921679967 97.72339631953372 6.1240477956834445
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 35
		"cluster1" 1 "cv[0]"
		"cluster13" 1 "cv[0]"
		"cluster13_1" 1 "cv[0]"
		"cluster14" 1 "cv[1]"
		"cluster14_1" 1 "cv[1]"
		"cluster15" 1 "cv[2]"
		"cluster15_1" 1 "cv[2]"
		"cluster16" 1 "cv[3]"
		"cluster16_1" 1 "cv[3]"
		"cluster17" 1 "cv[4]"
		"cluster17_1" 1 "cv[4]"
		"cluster18" 1 "cv[5]"
		"cluster18_1" 1 "cv[5]"
		"cluster19" 1 "cv[6]"
		"cluster19_1" 1 "cv[6]"
		"cluster1_1" 1 "cv[1]"
		"cluster1_10" 1 "cv[3]"
		"cluster1_11" 1 "cv[4]"
		"cluster1_12" 1 "cv[5]"
		"cluster1_13" 1 "cv[6]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[1]"
		"cluster1_16" 1 "cv[2]"
		"cluster1_17" 1 "cv[3]"
		"cluster1_18" 1 "cv[4]"
		"cluster1_19" 1 "cv[5]"
		"cluster1_2" 1 "cv[2]"
		"cluster1_20" 1 "cv[6]"
		"cluster1_3" 1 "cv[3]"
		"cluster1_4" 1 "cv[4]"
		"cluster1_5" 1 "cv[5]"
		"cluster1_6" 1 "cv[6]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[1]"
		"cluster1_9" 1 "cv[2]";
createNode nurbsCurve -n "lip_upper_frown_guideCrvShapeOrig1" -p "lip_upper_frown_guideCrv";
	rename -uid "43567DA1-40F6-FD3B-AF64-258FE9CB709D";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 2 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster26";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 2 "cv[0:2]" "cv[4:6]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster26_1";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 2 "cv[0:2]" "cv[4:6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028963088989 97.562576293945312 5.7681660652160645
		-1.3085188865661621 97.723396301269531 6.1240477561950684
		-0.76369941234588623 97.875625610351562 6.4950141906738281
		1.670394699563718e-19 97.929771423339844 6.7207808494567871
		0.76369941234588623 97.875625610351562 6.4950141906738281
		1.3085188865661621 97.723396301269531 6.1240477561950684
		1.7380028963088989 97.562576293945312 5.7681660652160645
		

		"gtag" 2
		"cluster26" 2 "cv[0:2]" "cv[4:6]"
		"cluster26_1" 2 "cv[0:2]" "cv[4:6]";
createNode transform -n "lip_lower_smile_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "4D5E5A2F-4C1F-0BBE-9D1E-48AAA8E8C656";
createNode nurbsCurve -n "lip_lower_smile_guideCrvShape" -p "lip_lower_smile_guideCrv";
	rename -uid "C624CEB7-4073-8A44-9705-85A399C01698";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_lower_smile_guideCrvShapeOrig" -p "lip_lower_smile_guideCrv";
	rename -uid "9213B498-44D2-1D7B-534E-61A5524D96D0";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 35 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster10";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster11";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster12";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster20";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster21";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster22";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster23";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster24";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.2576395445478417 97.402661377988451 6.024359840771357
		-0.73120154860842312 97.235717429291398 6.2578796389602918
		3.7669309661685105e-18 97.120437438767468 6.45093567580557
		0.73120154860842312 97.235717429291398 6.2578796389602918
		1.2576395445478417 97.402661377988451 6.024359840771357
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 35
		"cluster1" 1 "cv[0]"
		"cluster10" 1 "cv[4]"
		"cluster11" 1 "cv[5]"
		"cluster12" 1 "cv[6]"
		"cluster13" 1 "cv[0]"
		"cluster19" 1 "cv[6]"
		"cluster1_1" 1 "cv[6]"
		"cluster1_10" 1 "cv[4]"
		"cluster1_11" 1 "cv[3]"
		"cluster1_12" 1 "cv[2]"
		"cluster1_13" 1 "cv[1]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[6]"
		"cluster1_16" 1 "cv[5]"
		"cluster1_17" 1 "cv[4]"
		"cluster1_18" 1 "cv[3]"
		"cluster1_19" 1 "cv[2]"
		"cluster1_2" 1 "cv[5]"
		"cluster1_20" 1 "cv[1]"
		"cluster1_3" 1 "cv[4]"
		"cluster1_4" 1 "cv[3]"
		"cluster1_5" 1 "cv[2]"
		"cluster1_6" 1 "cv[1]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[6]"
		"cluster1_9" 1 "cv[5]"
		"cluster20" 1 "cv[5]"
		"cluster21" 1 "cv[4]"
		"cluster22" 1 "cv[3]"
		"cluster23" 1 "cv[2]"
		"cluster24" 1 "cv[1]"
		"cluster6" 1 "cv[0]"
		"cluster7" 1 "cv[1]"
		"cluster8" 1 "cv[2]"
		"cluster9" 1 "cv[3]";
createNode nurbsCurve -n "lip_lower_smile_guideCrvShapeOrig1" -p "lip_lower_smile_guideCrv";
	rename -uid "A61C946F-41E2-3A70-B15C-F4A17E8FB422";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "cluster25";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 2 "cv[0:2]" "cv[4:6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028963088989 97.562576293945312 5.7681660652160645
		-1.2576395273208618 97.402664184570312 6.0243597030639648
		-0.73120152950286865 97.2357177734375 6.2578797340393066
		3.7669308787297348e-18 97.120437622070312 6.4509358406066895
		0.73120152950286865 97.2357177734375 6.2578797340393066
		1.2576395273208618 97.402664184570312 6.0243597030639648
		1.7380028963088989 97.562576293945312 5.7681660652160645
		

		"gtag" 1
		"cluster25" 2 "cv[0:2]" "cv[4:6]";
createNode transform -n "lip_upper_smile_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "CF5ABB37-44CA-5617-2314-28800DBDBA71";
createNode nurbsCurve -n "lip_upper_smile_guideCrvShape" -p "lip_upper_smile_guideCrv";
	rename -uid "E44521E7-453C-2DED-3D7C-1398BB9537B6";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_upper_smile_guideCrvShapeOrig" -p "lip_upper_smile_guideCrv";
	rename -uid "A45AFA46-4250-85CC-38FC-E0833ACFA999";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 35 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster14";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster15";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster16";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster17";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster18";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13_1";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster14_1";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster15_1";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster16_1";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster17_1";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster18_1";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster19_1";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.3085188921679967 97.72339631953372 6.1240477956834445
		-0.76369939659500408 97.875628709476885 6.4950139526250359
		1.670394704933599e-19 97.929771954570768 6.7207808961601136
		0.76369939659500408 97.875628709476885 6.4950139526250359
		1.3085188921679967 97.72339631953372 6.1240477956834445
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 35
		"cluster1" 1 "cv[0]"
		"cluster13" 1 "cv[0]"
		"cluster13_1" 1 "cv[0]"
		"cluster14" 1 "cv[1]"
		"cluster14_1" 1 "cv[1]"
		"cluster15" 1 "cv[2]"
		"cluster15_1" 1 "cv[2]"
		"cluster16" 1 "cv[3]"
		"cluster16_1" 1 "cv[3]"
		"cluster17" 1 "cv[4]"
		"cluster17_1" 1 "cv[4]"
		"cluster18" 1 "cv[5]"
		"cluster18_1" 1 "cv[5]"
		"cluster19" 1 "cv[6]"
		"cluster19_1" 1 "cv[6]"
		"cluster1_1" 1 "cv[1]"
		"cluster1_10" 1 "cv[3]"
		"cluster1_11" 1 "cv[4]"
		"cluster1_12" 1 "cv[5]"
		"cluster1_13" 1 "cv[6]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[1]"
		"cluster1_16" 1 "cv[2]"
		"cluster1_17" 1 "cv[3]"
		"cluster1_18" 1 "cv[4]"
		"cluster1_19" 1 "cv[5]"
		"cluster1_2" 1 "cv[2]"
		"cluster1_20" 1 "cv[6]"
		"cluster1_3" 1 "cv[3]"
		"cluster1_4" 1 "cv[4]"
		"cluster1_5" 1 "cv[5]"
		"cluster1_6" 1 "cv[6]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[1]"
		"cluster1_9" 1 "cv[2]";
createNode nurbsCurve -n "lip_upper_smile_guideCrvShapeOrig1" -p "lip_upper_smile_guideCrv";
	rename -uid "8F93DFF9-48E6-5F34-E552-CAB9ACDBF8FA";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "cluster25";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 2 "cv[0:2]" "cv[4:6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028963088989 97.562576293945312 5.7681660652160645
		-1.3085188865661621 97.723396301269531 6.1240477561950684
		-0.76369941234588623 97.875625610351562 6.4950141906738281
		1.670394699563718e-19 97.929771423339844 6.7207808494567871
		0.76369941234588623 97.875625610351562 6.4950141906738281
		1.3085188865661621 97.723396301269531 6.1240477561950684
		1.7380028963088989 97.562576293945312 5.7681660652160645
		

		"gtag" 1
		"cluster25" 2 "cv[0:2]" "cv[4:6]";
createNode transform -n "lip_lower_wide_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "5C9E282C-49D9-8D99-F8DC-3F9E604613ED";
createNode nurbsCurve -n "lip_lower_wide_guideCrvShape" -p "lip_lower_wide_guideCrv";
	rename -uid "95C7E12D-440F-1976-9079-4B86341E6C7F";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_lower_wide_guideCrvShapeOrig" -p "lip_lower_wide_guideCrv";
	rename -uid "B7543431-461F-5EE8-FBA6-7A829F833605";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 35 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster10";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster11";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster12";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster20";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster21";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster22";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster23";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster24";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.2576395445478417 97.402661377988451 6.024359840771357
		-0.73120154860842312 97.235717429291398 6.2578796389602918
		3.7669309661685105e-18 97.120437438767468 6.45093567580557
		0.73120154860842312 97.235717429291398 6.2578796389602918
		1.2576395445478417 97.402661377988451 6.024359840771357
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 35
		"cluster1" 1 "cv[0]"
		"cluster10" 1 "cv[4]"
		"cluster11" 1 "cv[5]"
		"cluster12" 1 "cv[6]"
		"cluster13" 1 "cv[0]"
		"cluster19" 1 "cv[6]"
		"cluster1_1" 1 "cv[6]"
		"cluster1_10" 1 "cv[4]"
		"cluster1_11" 1 "cv[3]"
		"cluster1_12" 1 "cv[2]"
		"cluster1_13" 1 "cv[1]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[6]"
		"cluster1_16" 1 "cv[5]"
		"cluster1_17" 1 "cv[4]"
		"cluster1_18" 1 "cv[3]"
		"cluster1_19" 1 "cv[2]"
		"cluster1_2" 1 "cv[5]"
		"cluster1_20" 1 "cv[1]"
		"cluster1_3" 1 "cv[4]"
		"cluster1_4" 1 "cv[3]"
		"cluster1_5" 1 "cv[2]"
		"cluster1_6" 1 "cv[1]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[6]"
		"cluster1_9" 1 "cv[5]"
		"cluster20" 1 "cv[5]"
		"cluster21" 1 "cv[4]"
		"cluster22" 1 "cv[3]"
		"cluster23" 1 "cv[2]"
		"cluster24" 1 "cv[1]"
		"cluster6" 1 "cv[0]"
		"cluster7" 1 "cv[1]"
		"cluster8" 1 "cv[2]"
		"cluster9" 1 "cv[3]";
createNode nurbsCurve -n "lip_lower_wide_guideCrvShapeOrig1" -p "lip_lower_wide_guideCrv";
	rename -uid "43DF05E7-40F2-D2EC-D8E6-84A0EF49EBF0";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028963088989 97.562576293945312 5.7681660652160645
		-1.2576395273208618 97.402664184570312 6.0243597030639648
		-0.73120152950286865 97.2357177734375 6.2578797340393066
		3.7669308787297348e-18 97.120437622070312 6.4509358406066895
		0.73120152950286865 97.2357177734375 6.2578797340393066
		1.2576395273208618 97.402664184570312 6.0243597030639648
		1.7380028963088989 97.562576293945312 5.7681660652160645
		;
createNode transform -n "lip_upper_wide_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "ADDD718A-40C4-4851-762B-C2A759C95DCB";
createNode nurbsCurve -n "lip_upper_wide_guideCrvShape" -p "lip_upper_wide_guideCrv";
	rename -uid "9021611F-4798-2ECE-887E-E49860838358";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_upper_wide_guideCrvShapeOrig" -p "lip_upper_wide_guideCrv";
	rename -uid "20880E09-4CAE-6FAB-B1D8-C28F71664F48";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 35 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster14";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster15";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster16";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster17";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster18";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13_1";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster14_1";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster15_1";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster16_1";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster17_1";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster18_1";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster19_1";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.3085188921679967 97.72339631953372 6.1240477956834445
		-0.76369939659500408 97.875628709476885 6.4950139526250359
		1.670394704933599e-19 97.929771954570768 6.7207808961601136
		0.76369939659500408 97.875628709476885 6.4950139526250359
		1.3085188921679967 97.72339631953372 6.1240477956834445
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 35
		"cluster1" 1 "cv[0]"
		"cluster13" 1 "cv[0]"
		"cluster13_1" 1 "cv[0]"
		"cluster14" 1 "cv[1]"
		"cluster14_1" 1 "cv[1]"
		"cluster15" 1 "cv[2]"
		"cluster15_1" 1 "cv[2]"
		"cluster16" 1 "cv[3]"
		"cluster16_1" 1 "cv[3]"
		"cluster17" 1 "cv[4]"
		"cluster17_1" 1 "cv[4]"
		"cluster18" 1 "cv[5]"
		"cluster18_1" 1 "cv[5]"
		"cluster19" 1 "cv[6]"
		"cluster19_1" 1 "cv[6]"
		"cluster1_1" 1 "cv[1]"
		"cluster1_10" 1 "cv[3]"
		"cluster1_11" 1 "cv[4]"
		"cluster1_12" 1 "cv[5]"
		"cluster1_13" 1 "cv[6]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[1]"
		"cluster1_16" 1 "cv[2]"
		"cluster1_17" 1 "cv[3]"
		"cluster1_18" 1 "cv[4]"
		"cluster1_19" 1 "cv[5]"
		"cluster1_2" 1 "cv[2]"
		"cluster1_20" 1 "cv[6]"
		"cluster1_3" 1 "cv[3]"
		"cluster1_4" 1 "cv[4]"
		"cluster1_5" 1 "cv[5]"
		"cluster1_6" 1 "cv[6]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[1]"
		"cluster1_9" 1 "cv[2]";
createNode nurbsCurve -n "lip_upper_wide_guideCrvShapeOrig1" -p "lip_upper_wide_guideCrv";
	rename -uid "161501EC-4DC0-A1BE-8A2D-A984CC832588";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028963088989 97.562576293945312 5.7681660652160645
		-1.3085188865661621 97.723396301269531 6.1240477561950684
		-0.76369941234588623 97.875625610351562 6.4950141906738281
		1.670394699563718e-19 97.929771423339844 6.7207808494567871
		0.76369941234588623 97.875625610351562 6.4950141906738281
		1.3085188865661621 97.723396301269531 6.1240477561950684
		1.7380028963088989 97.562576293945312 5.7681660652160645
		;
createNode transform -n "lip_lower_small_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "F2870C1A-4863-99C7-D6F1-4AA03478D3C6";
createNode nurbsCurve -n "lip_lower_small_guideCrvShape" -p "lip_lower_small_guideCrv";
	rename -uid "19E41C44-44B0-9195-13A6-799DCB438496";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_lower_small_guideCrvShapeOrig" -p "lip_lower_small_guideCrv";
	rename -uid "BB22232B-48CF-6CE0-1B05-09909A33D090";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 35 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster10";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster11";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster12";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster20";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster21";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster22";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster23";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster24";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.2576395445478417 97.402661377988451 6.024359840771357
		-0.73120154860842312 97.235717429291398 6.2578796389602918
		3.7669309661685105e-18 97.120437438767468 6.45093567580557
		0.73120154860842312 97.235717429291398 6.2578796389602918
		1.2576395445478417 97.402661377988451 6.024359840771357
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 35
		"cluster1" 1 "cv[0]"
		"cluster10" 1 "cv[4]"
		"cluster11" 1 "cv[5]"
		"cluster12" 1 "cv[6]"
		"cluster13" 1 "cv[0]"
		"cluster19" 1 "cv[6]"
		"cluster1_1" 1 "cv[6]"
		"cluster1_10" 1 "cv[4]"
		"cluster1_11" 1 "cv[3]"
		"cluster1_12" 1 "cv[2]"
		"cluster1_13" 1 "cv[1]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[6]"
		"cluster1_16" 1 "cv[5]"
		"cluster1_17" 1 "cv[4]"
		"cluster1_18" 1 "cv[3]"
		"cluster1_19" 1 "cv[2]"
		"cluster1_2" 1 "cv[5]"
		"cluster1_20" 1 "cv[1]"
		"cluster1_3" 1 "cv[4]"
		"cluster1_4" 1 "cv[3]"
		"cluster1_5" 1 "cv[2]"
		"cluster1_6" 1 "cv[1]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[6]"
		"cluster1_9" 1 "cv[5]"
		"cluster20" 1 "cv[5]"
		"cluster21" 1 "cv[4]"
		"cluster22" 1 "cv[3]"
		"cluster23" 1 "cv[2]"
		"cluster24" 1 "cv[1]"
		"cluster6" 1 "cv[0]"
		"cluster7" 1 "cv[1]"
		"cluster8" 1 "cv[2]"
		"cluster9" 1 "cv[3]";
createNode nurbsCurve -n "lip_lower_small_guideCrvShapeOrig1" -p "lip_lower_small_guideCrv";
	rename -uid "BA88655E-43F8-1B73-3108-7D8595D3AC4C";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028963088989 97.562576293945312 5.7681660652160645
		-1.2576395273208618 97.402664184570312 6.0243597030639648
		-0.73120152950286865 97.2357177734375 6.2578797340393066
		3.7669308787297348e-18 97.120437622070312 6.4509358406066895
		0.73120152950286865 97.2357177734375 6.2578797340393066
		1.2576395273208618 97.402664184570312 6.0243597030639648
		1.7380028963088989 97.562576293945312 5.7681660652160645
		;
createNode transform -n "lip_upper_small_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "E67C6887-419A-5B8C-F705-B390F5843CC9";
createNode nurbsCurve -n "lip_upper_small_guideCrvShape" -p "lip_upper_small_guideCrv";
	rename -uid "FE075376-4F7E-A060-A600-D8B4908693DD";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_upper_small_guideCrvShapeOrig" -p "lip_upper_small_guideCrv";
	rename -uid "622C7399-412E-BF5F-245C-AA963322C5BA";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 35 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster14";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster15";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster16";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster17";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster18";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[28].gtagnm" -type "string" "cluster13_1";
	setAttr ".gtag[28].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[29].gtagnm" -type "string" "cluster14_1";
	setAttr ".gtag[29].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[30].gtagnm" -type "string" "cluster15_1";
	setAttr ".gtag[30].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[31].gtagnm" -type "string" "cluster16_1";
	setAttr ".gtag[31].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[32].gtagnm" -type "string" "cluster17_1";
	setAttr ".gtag[32].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[33].gtagnm" -type "string" "cluster18_1";
	setAttr ".gtag[33].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[34].gtagnm" -type "string" "cluster19_1";
	setAttr ".gtag[34].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028942770758 97.562577257204225 5.7681658765326533
		-1.3085188921679967 97.72339631953372 6.1240477956834445
		-0.76369939659500408 97.875628709476885 6.4950139526250359
		1.670394704933599e-19 97.929771954570768 6.7207808961601136
		0.76369939659500408 97.875628709476885 6.4950139526250359
		1.3085188921679967 97.72339631953372 6.1240477956834445
		1.7380028942770758 97.562577257204225 5.7681658765326533
		

		"gtag" 35
		"cluster1" 1 "cv[0]"
		"cluster13" 1 "cv[0]"
		"cluster13_1" 1 "cv[0]"
		"cluster14" 1 "cv[1]"
		"cluster14_1" 1 "cv[1]"
		"cluster15" 1 "cv[2]"
		"cluster15_1" 1 "cv[2]"
		"cluster16" 1 "cv[3]"
		"cluster16_1" 1 "cv[3]"
		"cluster17" 1 "cv[4]"
		"cluster17_1" 1 "cv[4]"
		"cluster18" 1 "cv[5]"
		"cluster18_1" 1 "cv[5]"
		"cluster19" 1 "cv[6]"
		"cluster19_1" 1 "cv[6]"
		"cluster1_1" 1 "cv[1]"
		"cluster1_10" 1 "cv[3]"
		"cluster1_11" 1 "cv[4]"
		"cluster1_12" 1 "cv[5]"
		"cluster1_13" 1 "cv[6]"
		"cluster1_14" 1 "cv[0]"
		"cluster1_15" 1 "cv[1]"
		"cluster1_16" 1 "cv[2]"
		"cluster1_17" 1 "cv[3]"
		"cluster1_18" 1 "cv[4]"
		"cluster1_19" 1 "cv[5]"
		"cluster1_2" 1 "cv[2]"
		"cluster1_20" 1 "cv[6]"
		"cluster1_3" 1 "cv[3]"
		"cluster1_4" 1 "cv[4]"
		"cluster1_5" 1 "cv[5]"
		"cluster1_6" 1 "cv[6]"
		"cluster1_7" 1 "cv[0]"
		"cluster1_8" 1 "cv[1]"
		"cluster1_9" 1 "cv[2]";
createNode nurbsCurve -n "lip_upper_small_guideCrvShapeOrig1" -p "lip_upper_small_guideCrv";
	rename -uid "DE10C700-446F-EE2C-FBE1-A6AC0BA08DEB";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-1.7380028963088989 97.562576293945312 5.7681660652160645
		-1.3085188865661621 97.723396301269531 6.1240477561950684
		-0.76369941234588623 97.875625610351562 6.4950141906738281
		1.670394699563718e-19 97.929771423339844 6.7207808494567871
		0.76369941234588623 97.875625610351562 6.4950141906738281
		1.3085188865661621 97.723396301269531 6.1240477561950684
		1.7380028963088989 97.562576293945312 5.7681660652160645
		;
createNode transform -n "lid_upper_open_r_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "829E4B31-4990-BACE-EE7A-5A8FF7BA8A77";
createNode nurbsCurve -n "lid_upper_open_r_guideCrvShape" -p "lid_upper_open_r_guideCrv";
	rename -uid "CA91084A-4FF7-5125-DB53-8F824229D09A";
	setAttr -k off ".v";
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "lid_upper_open_r_guideCrvShapeOrig" -p "lid_upper_open_r_guideCrv";
	rename -uid "3BEDB386-4926-12C6-91BB-BE9B032D18EB";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 5 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster2";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster3";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster4";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster5";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".cc" -type "nurbsCurve" 
		2 3 0 no 3
		6 0 0 0.33333333333333337 0.66666666666666674 1 1
		5
		-1.6306558404308684 101.9526128673328 6.0392417907714844
		-1.8873145991642415 102.70483066528182 6.4376478179797871
		-3.0241072214444942 103.14755964870648 6.5843792242413191
		-3.9834420987961319 102.85642513926248 6.0141117327555849
		-4.2763590812683105 102.36575814485055 5.4278616905212402
		

		"gtag" 5
		"cluster1" 1 "cv[0]"
		"cluster2" 1 "cv[1]"
		"cluster3" 1 "cv[2]"
		"cluster4" 1 "cv[3]"
		"cluster5" 1 "cv[4]";
createNode transform -n "lid_lower_open_r_guideCrv" -p "NOTOUCH_crv_Grp";
	rename -uid "9A7604C7-456B-EDE4-C45B-909FC7957E2B";
createNode nurbsCurve -n "lid_lower_open_r_guideCrvShape" -p "lid_lower_open_r_guideCrv";
	rename -uid "191BCAD5-410A-71CE-2685-58B3A5D5D572";
	setAttr -k off ".v";
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "lid_lower_open_r_guideCrvShapeOrig" -p "lid_lower_open_r_guideCrv";
	rename -uid "95FA8B6B-42FA-35F6-3FF3-81A78B6BF086";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 5 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster20";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster21";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster22";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster23";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster24";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".cc" -type "nurbsCurve" 
		2 3 0 no 3
		6 0 0 0.33333333333333337 0.66666666666666674 1 1
		5
		-1.6306558404308684 101.9526128673328 6.0392417907714844
		-2.2685830173039618 101.83709244633017 6.2494789684471135
		-3.1095689168870786 101.70172134613753 6.2902151540887123
		-4.0393744896243549 101.97178108066886 5.8298720770307177
		-4.2763590812683105 102.36575814485055 5.4278616905212402
		

		"gtag" 5
		"cluster20" 1 "cv[0]"
		"cluster21" 1 "cv[1]"
		"cluster22" 1 "cv[2]"
		"cluster23" 1 "cv[3]"
		"cluster24" 1 "cv[4]";
createNode transform -n "NOTOUCH_cls_Grp" -p "NOTOUCH";
	rename -uid "C8970224-49F7-092F-EDD5-DAB5AAF8B543";
	setAttr ".v" no;
createNode transform -n "lip_follow_00" -p "NOTOUCH_cls_Grp";
	rename -uid "4B3D9838-47BD-BA36-5DBC-CBBC65587B12";
	setAttr ".rp" -type "double3" 0.76369941234588623 97.875625610351562 6.4950141906738281 ;
	setAttr ".sp" -type "double3" 0.76369941234588623 97.875625610351562 6.4950141906738281 ;
createNode clusterHandle -n "lip_follow_00Shape" -p "lip_follow_00";
	rename -uid "DDA27B44-42D6-F528-1ABA-EDA7B16D46EB";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0.76369941234588623 97.875625610351562 6.4950141906738281 ;
createNode transform -n "lip_follow_01" -p "NOTOUCH_cls_Grp";
	rename -uid "FEE6784E-4B76-A7F0-B1EA-58B470A40369";
	setAttr ".rp" -type "double3" 1.3085188865661621 97.723396301269531 6.1240477561950684 ;
	setAttr ".sp" -type "double3" 1.3085188865661621 97.723396301269531 6.1240477561950684 ;
createNode clusterHandle -n "lip_follow_01Shape" -p "lip_follow_01";
	rename -uid "9CEB7C26-4BC0-E033-0935-47912D75A925";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.3085188865661621 97.723396301269531 6.1240477561950684 ;
createNode transform -n "lip_follow_02" -p "NOTOUCH_cls_Grp";
	rename -uid "B65383D1-4304-96CB-007E-5B8536438A77";
	setAttr ".rp" -type "double3" 1.7380028963088989 97.562576293945312 5.7681660652160645 ;
	setAttr ".sp" -type "double3" 1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode clusterHandle -n "lip_follow_02Shape" -p "lip_follow_02";
	rename -uid "446CCCC8-43E1-F262-07EF-60837870E6F3";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode transform -n "lip_follow_03" -p "NOTOUCH_cls_Grp";
	rename -uid "F29EEBDA-4410-FC89-A907-7DA85B960CC2";
	setAttr ".rp" -type "double3" 1.2576395273208618 97.402664184570312 6.0243597030639648 ;
	setAttr ".sp" -type "double3" 1.2576395273208618 97.402664184570312 6.0243597030639648 ;
createNode clusterHandle -n "lip_follow_03Shape" -p "lip_follow_03";
	rename -uid "6621CAE4-438F-60FB-D629-4894CC288815";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.2576395273208618 97.402664184570312 6.0243597030639648 ;
createNode transform -n "lip_follow_04" -p "NOTOUCH_cls_Grp";
	rename -uid "6D0CAAB7-4094-C84D-5B1E-91866EB3BE3A";
	setAttr ".rp" -type "double3" 0.73120152950286865 97.2357177734375 6.2578797340393066 ;
	setAttr ".sp" -type "double3" 0.73120152950286865 97.2357177734375 6.2578797340393066 ;
createNode clusterHandle -n "lip_follow_04Shape" -p "lip_follow_04";
	rename -uid "05462E1C-4C73-F267-5734-FF867A7C5ED1";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0.73120152950286865 97.2357177734375 6.2578797340393066 ;
createNode transform -n "lip_follow_05" -p "NOTOUCH_cls_Grp";
	rename -uid "A3B361A6-4934-5907-3A7B-199CF333E3FE";
	setAttr ".s" -type "double3" 1.5 1 1 ;
	setAttr ".rp" -type "double3" 0 97.525104522705078 6.2444734573364258 ;
	setAttr ".sp" -type "double3" 0 97.525104522705078 6.2444734573364258 ;
createNode clusterHandle -n "lip_follow_05Shape" -p "lip_follow_05";
	rename -uid "F0476B22-437D-47F9-6899-5EA906C20E6F";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 97.525104522705078 6.2444734573364258 ;
createNode transform -n "lip_follow_06" -p "NOTOUCH_cls_Grp";
	rename -uid "0C1E7101-4363-7FCB-CFE3-C2B2FCCE69B7";
	setAttr ".s" -type "double3" 0.5 1 1 ;
	setAttr ".rp" -type "double3" 0 97.525104522705078 6.2444734573364258 ;
	setAttr ".sp" -type "double3" 0 97.525104522705078 6.2444734573364258 ;
createNode clusterHandle -n "lip_follow_06Shape" -p "lip_follow_06";
	rename -uid "DF1B4481-428B-8F45-F21C-B4804EB3DC95";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 97.525104522705078 6.2444734573364258 ;
createNode transform -n "lip_follow_07" -p "NOTOUCH_cls_Grp";
	rename -uid "7EAF9644-4BC1-60B3-19BD-F88A9577F1E5";
	setAttr ".t" -type "double3" 0 -1 0 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 97.555671691894531 6.1315901279449463 ;
	setAttr ".sp" -type "double3" 0 97.555671691894531 6.1315901279449463 ;
createNode clusterHandle -n "lip_follow_07Shape" -p "lip_follow_07";
	rename -uid "7ED04D7F-4FF1-A060-139C-5698CBE98E62";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 97.555671691894531 6.1315901279449463 ;
createNode transform -n "lip_follow_08" -p "NOTOUCH_cls_Grp";
	rename -uid "E6ABB0CE-470B-C36A-069F-4D96B7B46DCC";
	setAttr ".t" -type "double3" 0 1 0 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 97.555671691894531 6.1315901279449463 ;
	setAttr ".sp" -type "double3" 0 97.555671691894531 6.1315901279449463 ;
createNode clusterHandle -n "lip_follow_08Shape" -p "lip_follow_08";
	rename -uid "65CDF03D-4785-B44B-9256-069130EC81D6";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 97.555671691894531 6.1315901279449463 ;
createNode transform -n "face_BIND_Grp";
	rename -uid "BCDCAE98-42CE-B04E-5573-B2852C54FA1C";
createNode joint -n "teeth_lower_bind" -p "face_BIND_Grp";
	rename -uid "4E691E17-4731-09A8-1F14-94B80E84574E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 1.989981936829574e-15 96.993590202620823 5.3547644030562918 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 6.5376777919745086 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.9805212901035405 0.19641282965653939 0
		 0 -0.19641282965653939 0.9805212901035405 0 0.013299211103944053 138.10891582416616 7.2178271315535767 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "teeth_lower_bind";
	setAttr ".radi" 0.2;
createNode joint -n "teeth_upper_bind" -p "face_BIND_Grp";
	rename -uid "94647FEA-4CAC-E590-B025-0881865668A7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.013299210928382481 98.386172208167125 6.5562535820716867 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".is" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.98052129010354039 0.19641282965653928 0
		 0 -0.19641282965653928 0.98052129010354039 0 0.013299210928380489 138.11293712846211 7.0540576876644634 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "teeth_upper_bind";
	setAttr ".radi" 0.2;
createNode joint -n "tongue_01_bind" -p "face_BIND_Grp";
	rename -uid "2AAC5B5C-42F8-A381-63B3-BF92534E8DE6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 1.9899819368295736e-15 97.098712879469261 3.4761210207375486 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.577674211802957 -64.581845045189851 89.618554356893895 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_02_bind" -p "tongue_01_bind";
	rename -uid "CF6C5112-4CF4-B3CD-82DB-EDBBF0229867";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.61247032276244084 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.043325316350068248 -0.18838287833144113 -12.465555236274424 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_03_bind" -p "tongue_02_bind";
	rename -uid "EFBC012C-4565-9DC8-8D66-60B4F28C3F53";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.65907319232506367 1.4210854715202004e-14 1.474514954580286e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.00014551855653038924 0.0025563080207655093 -6.5161244795551916 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_04_bind" -p "tongue_03_bind";
	rename -uid "1AC01B51-44E2-857C-369D-B79D1B14112E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.63449551202333865 -1.4210854715202004e-14 1.5178830414797062e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.9877521080445241e-05 -0.0020099932944911713 -3.4126630577571095 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_05_bind" -p "tongue_04_bind";
	rename -uid "80FC3982-4EA2-4B58-1FB1-2294452852CE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.58745991403572262 -2.8421709430404007e-14 8.6736173798840355e-19 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.00035490689171974497 0.014237736791363096 -2.662717444288174 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_06_bind" -p "tongue_05_bind";
	rename -uid "1F2987D9-4B22-19A6-0AC8-26B31EB9D47F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.43079789301606208 -1.4210854715202004e-14 -7.589415207398531e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.0012898873536458767 0.018933565599269057 -4.2577920543636401 ;
	setAttr ".radi" 0.2;
createNode joint -n "tongue_07_bind" -p "tongue_06_bind";
	rename -uid "A827738C-4CA6-6FA3-D5E2-FF9501C79813";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.38893662555992314 2.8421709430404007e-14 -3.0357660829594124e-18 ;
	setAttr ".r" -type "double3" 6.1224124612957134e-14 2.4425666030301852e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".radi" 0.2;
createNode joint -n "face_bind" -p "face_BIND_Grp";
	rename -uid "CFDADF63-454A-50EB-9FE1-AF8A7A6F86E8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 3.3019790515124298e-14 100 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3019790515124298e-14 139.54475402832031 -2 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_bind";
	setAttr ".radi" 0.3;
	setAttr ".liw" yes;
createNode joint -n "face_upper_bind" -p "face_bind";
	rename -uid "BE297977-46BE-92CC-E3B5-F68C253B6DA2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -3.1029095486420873e-14 -0.1508558961503752 0.3 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1.0000000000000002 0 7.1309187385013778e-19 141.53578757853617 -1.7 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_upper_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "eye_socket_l_bind" -p "face_upper_bind";
	rename -uid "4217BC4E-4C3C-0E26-792B-5CA3D74296A1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.8499724750393103 2.4711015923378596 5.2508923218665879 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.6800000667572021 144.65299987792969 1.9069999456405642 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye_socket";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "eye_l_bind" -p "eye_socket_l_bind";
	rename -uid "07B2D839-4455-D1D4-0A4E-0BB9FBDB1B47";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.6800000667572035 144.65299987792966 1.9069999456405637 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
	setAttr ".radi" 0.2;
createNode joint -n "eye_socket_r_bind" -p "face_upper_bind";
	rename -uid "0E307F9E-44E1-3E61-C9A4-E08C71426168";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -2.8499724750393103 2.4711015923378596 5.2508923218665879 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 0 -1.2246467991473532e-16 0 0 1 0 0 1.2246467991473532e-16 0 -1 0
		 -3.6800000667572021 144.65299987792969 1.9069999456405642 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye_socket";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "eye_r_bind" -p "eye_socket_r_bind";
	rename -uid "FEDDA1F6-4665-EBC9-BE23-CF9CF3548748";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 2.4492935982947064e-16 0 0 1 0 0 -2.4492935982947064e-16 0 1 0
		 -3.6800000667571995 144.65299987792969 1.9069999456405644 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
	setAttr ".radi" 0.2;
createNode joint -n "nose_bridge_bind" -p "face_upper_bind";
	rename -uid "35A539EB-4DA3-6931-F996-5B8378A70968";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 2 7 ;
	setAttr ".r" -type "double3" -25 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99996192306476117 0.0078949694251991553 -0.0037177786916076381 0
		 -0.00872653543077671 0.9046738962540336 -0.42601524505106786 0 -2.1684043449710093e-19 0.42603146702364741 0.90470834477508766 0
		 -0.019507717542005941 143.86306330870656 7.8343620802521761 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nose_brige_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "nose_bind" -p "nose_bridge_bind";
	rename -uid "3F7A1C7A-4436-EFF0-930C-8BB129DDF908";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 -1.5 7.1054273576010019e-15 ;
	setAttr ".r" -type "double3" 20 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -6.9388939039072284e-18 4.3368086899420177e-18 0
		 6.8533465540116807e-18 0.99940289822345529 -0.034552091435368637 0 -3.6686991162046965e-18 0.034552091435368693 0.99940289822345529 0
		 -5.2041704279304213e-16 141.93141255994448 8.9694147686645316 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nose_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "sneer_l_bind" -p "nose_bind";
	rename -uid "A182E6B9-4615-2050-DA01-F8B4A11D5C05";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.20000000298023224 2.8421709430404007e-14 -3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 0 0 -20 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 -6.9388939039072284e-18 4.3368086899420177e-18 0
		 7.5896831226623083e-18 0.95289882536415571 -0.30328835885937405 0 -1.6806017649044133e-18 0.30328835885937411 0.95289882536415571 0
		 0.21903214560501705 141.93141255994448 8.969414768664528 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "sneer";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "nostril_l_bind" -p "sneer_l_bind";
	rename -uid "78640DCF-470B-4FF7-AA56-C19A394B4F1B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -0.99999999999998579 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.97635641039468091 0.20598525391636685 -0.065560926245923301 0
		 -0.21616697222566983 0.93036887660185497 -0.29611753337043228 0 -1.6806017649044133e-18 0.30328835885937411 0.95289882536415571 0
		 0.49003214560504404 141.17998936799685 9.4803797250003345 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nostril";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "sneer_r_bind" -p "nose_bind";
	rename -uid "6322E754-40FD-1305-DCC6-E6AB3F947611";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -0.2 2.8421709430404007e-14 -3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 0 0 -20 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 2.7074830858901341e-18 -1.2672836472673628e-16 0
		 4.0677231322670454e-17 0.95289953436686914 -0.30328613124144665 0 1.1959080448209269e-16 -0.30328613124144671 -0.95289953436686925 0
		 -0.2190319999999962 141.93111672133057 8.9693909197842583 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "sneer";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "nostril_r_bind" -p "sneer_r_bind";
	rename -uid "60F862C4-4108-F542-48A5-C6BD3BDC0910";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -7.1054273576010019e-15 -0.99999999999995737 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.97635641039468091 0.20598540717933672 -0.065560444708500781 0
		 0.21616697222566986 0.93036956884119926 -0.29611535842138892 0 1.1959080448209269e-16 -0.30328613124144671 -0.95289953436686925 0
		 -0.49003200000001745 141.1796923348885 9.480354119496571 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nostril";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_r_bind" -p "face_upper_bind";
	rename -uid "C229D211-4B6B-F31E-78A4-31B3833C4A66";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.4146180152893066 4.0503157350175627 6.7629809498786901 ;
	setAttr ".r" -type "double3" 0 -17.00000000000006 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_peak_r_bind" -p "brow_r_bind";
	rename -uid "003ACE12-450B-71BC-6313-D49A7066C446";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 1.4215945517698252 0.40148925781251421 0.31068968998799384 ;
	setAttr ".r" -type "double3" 0 -8.0000000000000551 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_peak";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_inner_r_bind" -p "brow_r_bind";
	rename -uid "459B31C6-43E6-8626-F940-73B3EF21BD73";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 3.5580569057404179 0.13508605957032671 0.075983850791793373 ;
	setAttr ".r" -type "double3" 0 17.000000000000011 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 0 0
		 0 0 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_inner";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_corrugator_r_bind" -p "brow_inner_r_bind";
	rename -uid "60F06A51-41E0-3119-8F56-36BEAB6FD944";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -0.58711922168731689 0.4221038818359375 0.048930168151857245 ;
	setAttr ".r" -type "double3" 0 0 14.999999999999998 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.96592582628906831 -0.25881904510252052 -1.2246467991473532e-16 0
		 -0.25881904510252052 0.96592582628906842 3.0814879110195774e-33 0 1.1829179713786698e-16 3.1696191514317612e-17 -1 0
		 -3.1426379680633545 147.62466326971466 8.3068027496337891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_corrugator";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_l_bind" -p "face_upper_bind";
	rename -uid "8628B213-4C0A-4449-AFAB-C79225A48387";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.4146180152893066 4.0503157350175627 6.7629809498786901 ;
	setAttr ".r" -type "double3" 0 17 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_peak_l_bind" -p "brow_l_bind";
	rename -uid "D40371A7-466F-8E1E-9AB3-45BF09DF1FCD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.4215945517698256 0.4014892578125 -0.31068968772888184 ;
	setAttr ".r" -type "double3" 0 8 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_peak";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_inner_l_bind" -p "brow_l_bind";
	rename -uid "E8B5B3FE-41A6-5273-EDB6-ADB1F3D259C2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.5580569057404197 0.1350860595703125 -0.07598385214805603 ;
	setAttr ".r" -type "double3" 0 -17 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 0 0
		 0 0 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_inner";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "brow_corrugator_l_bind" -p "brow_inner_l_bind";
	rename -uid "29DCED77-4A8E-2B41-091D-24A0A4826A31";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.58711922168731689 0.4221038818359375 -0.048930168151857245 ;
	setAttr ".r" -type "double3" 0 0 14.999999999999998 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.96592582628906831 -0.25881904510252052 -1.2246467991473532e-16 0
		 -0.25881904510252052 0.96592582628906842 3.0814879110195774e-33 0 1.1829179713786698e-16 3.1696191514317612e-17 -1 0
		 -3.1426379680633545 147.62466326971466 8.3068027496337891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_corrugator";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "face_lower_bind" -p "face_bind";
	rename -uid "12046A0A-48C1-1964-6167-A1AF43E39981";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 1.2348983868225787 0.23811262572524838 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 142.92154186150913 -1.7 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_lower_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "jaw_trans_bind" -p "face_lower_bind";
	rename -uid "65E23A9F-4488-2D85-637E-DB9EA47D46DF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 -1.6262223533614701 -0.37528104248188243 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 141.29531950814766 -0.89218694903278761 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "jaw_trans_bind";
	setAttr ".radi" 0.2;
createNode joint -n "jaw_bind" -p "jaw_trans_bind";
	rename -uid "10568A45-48A1-6473-C82A-94AC3E9DA72E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 1.4210854715202004e-14 7.5495165674510645e-15 ;
	setAttr ".r" -type "double3" 14.999999999999998 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "zyx";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96126169593831889 0.27563735581699911 0
		 0 -0.27563735581699911 0.96126169593831889 0 0 141.29531950814768 -0.89218694903278006 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "jaw_bind";
	setAttr ".radi" 0.2;
	setAttr ".liw" yes;
createNode joint -n "jaw_tip_bind" -p "jaw_bind";
	rename -uid "829A6B05-4F49-8104-8BE4-6A8F68EA9648";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -6.3108872417680944e-30 -1.4210854715202004e-14 5 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.98052129010354039 0.19641282965653953 0
		 0 -0.19641282965653953 0.98052129010354039 0 0 146.72480613686366 6.7018096387646464 1;
	setAttr ".radi" 0.2;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "C203AF16-4FD5-07B6-E254-9493F700DFF9";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "4E849815-4BDE-6DA3-7C2D-5CAA3D6BBA62";
	setAttr ".bsdt[0].bscd" -type "Int32Array" 12 0 1 2 3 4
		 5 6 7 8 9 10 11 ;
	setAttr -s 12 ".bspr";
	setAttr -s 12 ".obsv";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "3E6983DB-45C6-41C4-4853-D491BDB6E884";
createNode displayLayerManager -n "layerManager";
	rename -uid "F75AFD65-491E-76E6-2B2A-6182AB427624";
	setAttr ".cdl" 1;
	setAttr -s 2 ".dli[1]"  1;
	setAttr -s 2 ".dli";
createNode displayLayer -n "defaultLayer";
	rename -uid "CD90B0CD-41FB-C9C5-89C6-DF92BC3B2AFB";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "7E8FC101-40BE-B46E-3316-A3A7E5C4837E";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "D3F692CF-4E7E-D3F7-08D2-2FA44982A031";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "09FBCD70-47BA-7572-5332-ABB06E9EA3DE";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 574\n            -height 345\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 1\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 574\n            -height 345\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1155\n            -height 734\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1155\n            -height 734\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n"
		+ "            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n"
		+ "            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n"
		+ "            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n"
		+ "            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n"
		+ "                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n"
		+ "                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n"
		+ "                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -keyMinScale 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 0\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n"
		+ "                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n"
		+ "                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n"
		+ "                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n"
		+ "            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n"
		+ "                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n"
		+ "                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"|persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n"
		+ "                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n"
		+ "                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n"
		+ "        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1155\\n    -height 734\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1155\\n    -height 734\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 50 -size 100 -divisions 3 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "2895A3EC-41BB-018A-A872-758E37F9EEE6";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode blendShape -n "blendShape1";
	rename -uid "93963B27-4114-C46C-AA1F-BB8E6FD0D806";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  -0.60000002;
	setAttr ".mlid" 0;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lid_closed_r_guide","weight[0]"} ;
createNode blendShape -n "blendShape2";
	rename -uid "529B0B91-4A53-4FCC-95D5-10AC33609E2F";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  -0.69999999;
	setAttr ".mlid" 1;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lid_closed_r_guide","weight[0]"} ;
createNode cluster -n "lid_01_clst";
	rename -uid "46E5DC9C-40E6-E7F2-49AF-73B684CE037A";
	setAttr -s 3 ".ip";
	setAttr ".ip[0].gtg" -type "string" "cluster2";
	setAttr ".ip[1].gtg" -type "string" "cluster2_1";
	setAttr ".ip[2].gtg" -type "string" "cluster2";
	setAttr -s 3 ".og";
	setAttr -s 3 ".orggeom";
	setAttr -s 3 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_07Cluster";
	rename -uid "05575309-4032-650A-DAC5-7396689B32F0";
	setAttr -s 3 ".ip";
	setAttr ".ip[0].gtg" -type "string" "cluster3";
	setAttr ".ip[1].gtg" -type "string" "cluster3_1";
	setAttr ".ip[2].gtg" -type "string" "cluster3";
	setAttr -s 3 ".og";
	setAttr -s 3 ".orggeom";
	setAttr -s 3 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_01Cluster";
	rename -uid "E49C9449-45B4-C3EC-9CCB-B5A1F5DE3127";
	setAttr ".ip[0].gtg" -type "string" "cluster4_1";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_02Cluster";
	rename -uid "4B190C6B-4211-8CDC-8F8A-80A6790A9089";
	setAttr ".ip[0].gtg" -type "string" "cluster5_1";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_03Cluster";
	rename -uid "96CB17BE-4E17-0001-BE03-BCA6C6FE9ADB";
	setAttr ".ip[0].gtg" -type "string" "cluster6";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_09Cluster";
	rename -uid "BCC64A98-4FE4-7E5D-3948-F7BCEDB28319";
	setAttr ".ip[0].gtg" -type "string" "cluster7";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_08Cluster";
	rename -uid "E9D0E7EE-44F4-0A01-EC52-73B8ECE4E10A";
	setAttr ".ip[0].gtg" -type "string" "cluster8";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_10Cluster";
	rename -uid "4273C07A-4EC9-2BEC-1E44-AC8E4AD4155A";
	setAttr ".ip[0].gtg" -type "string" "cluster9";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_06Cluster";
	rename -uid "E1792B44-4108-757D-9DF6-71BD4A3B5712";
	setAttr ".ip[0].gtg" -type "string" "cluster10";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_05Cluster";
	rename -uid "D52C6AD4-4EDB-E241-F941-7BA3632CD909";
	setAttr ".ip[0].gtg" -type "string" "cluster11";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lid_handle_04Cluster";
	rename -uid "FCA3C305-4817-0DF4-05F8-83A98A7FC688";
	setAttr ".ip[0].gtg" -type "string" "cluster12";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_handle_03Cluster";
	rename -uid "C51F4475-469B-2741-507E-16945C960A68";
	setAttr -s 2 ".ip";
	setAttr ".ip[0].gtg" -type "string" "cluster13_1";
	setAttr ".ip[1].gtg" -type "string" "cluster13";
	setAttr -s 2 ".og";
	setAttr -s 2 ".orggeom";
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_handle_02Cluster";
	rename -uid "2E32113D-40E8-EEBC-60CF-72BC9FE36696";
	setAttr ".ip[0].gtg" -type "string" "cluster14_1";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_handle_01Cluster";
	rename -uid "3C04DFB2-4D3A-540F-49FE-6FADC599FFA9";
	setAttr ".ip[0].gtg" -type "string" "cluster15_1";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_handle_00Cluster";
	rename -uid "E6B1BE56-4BF0-BCA8-D87D-0FB818B0549C";
	setAttr ".ip[0].gtg" -type "string" "cluster16_1";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_follow_00Cluster";
	rename -uid "F7160849-4A7D-080B-BACB-8499B54D9E26";
	setAttr ".ip[0].gtg" -type "string" "cluster17_1";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_follow_01Cluster";
	rename -uid "DB08B190-4202-D3C6-1300-C4B1AB71C6C8";
	setAttr ".ip[0].gtg" -type "string" "cluster18_1";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_follow_02Cluster";
	rename -uid "5CF7E9E2-4765-4FEF-A000-EB82D89A6C7E";
	setAttr -s 2 ".ip";
	setAttr ".ip[0].gtg" -type "string" "cluster19_1";
	setAttr ".ip[1].gtg" -type "string" "cluster19";
	setAttr -s 2 ".og";
	setAttr -s 2 ".orggeom";
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_follow_03Cluster";
	rename -uid "85177829-4575-C3C6-5259-E08CAEB2620C";
	setAttr ".ip[0].gtg" -type "string" "cluster20";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_follow_04Cluster";
	rename -uid "9D7A99F3-41D4-3F57-E8B5-F9B038342D58";
	setAttr ".ip[0].gtg" -type "string" "cluster21";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_handle_06Cluster";
	rename -uid "E9EBB137-416E-1214-80B7-3A8E9C8FF8C3";
	setAttr ".ip[0].gtg" -type "string" "cluster22";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_handle_05Cluster";
	rename -uid "3B226D15-41C9-BDE7-6B9B-3DB958B93841";
	setAttr ".ip[0].gtg" -type "string" "cluster23";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_handle_04Cluster";
	rename -uid "F3A66492-4F62-3113-BFAD-77817E382DF9";
	setAttr ".ip[0].gtg" -type "string" "cluster24";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode multDoubleLinear -n "multDoubleLinear1";
	rename -uid "0A36CA26-47F8-F455-FAEA-20A36BBE1263";
	setAttr ".i2" -1;
createNode multDoubleLinear -n "multDoubleLinear2";
	rename -uid "68409787-4530-9DDE-2E2B-81A46645F504";
	setAttr ".i2" -1;
createNode multDoubleLinear -n "multDoubleLinear3";
	rename -uid "9BE16C48-4386-5069-5412-EA8709F46283";
	setAttr ".i2" -1;
createNode multDoubleLinear -n "multDoubleLinear4";
	rename -uid "01E48623-45AE-8EBB-D9E6-478FD6DB3899";
	setAttr ".i2" -1;
createNode multDoubleLinear -n "multDoubleLinear5";
	rename -uid "0E8FB839-48E6-82EC-44F5-4CBAA71F8EBD";
	setAttr ".i2" -1;
createNode displayLayer -n "noSelect";
	rename -uid "F0CA737B-471A-80DE-98C1-B2B11BB70CEF";
	setAttr ".dt" 1;
	setAttr ".do" 1;
createNode blendShape -n "blendShape3";
	rename -uid "53B7CDFB-444F-2549-3DB0-BC8E1BF04EC9";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 2;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".dfo" 1;
	setAttr ".aal" -type "attributeAlias" {"lid_upper_r_guide","weight[0]"} ;
createNode blendShape -n "blendShape4";
	rename -uid "29BA529B-40F9-A3DF-2639-7DB91C3D79D7";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 3;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".dfo" 1;
	setAttr ".aal" -type "attributeAlias" {"lid_lower_r_guide","weight[0]"} ;
createNode blendShape -n "blendShape5";
	rename -uid "D8EDA467-4D20-677B-DA32-3B91E005A1EC";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 4;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lip_upper_guide","weight[0]"} ;
createNode blendShape -n "blendShape6";
	rename -uid "9D90D6BB-44CC-02DD-A33F-2C979AE15F33";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 5;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lip_lower_guide","weight[0]"} ;
createNode cluster -n "lip_follow_08Cluster";
	rename -uid "E83763A1-4BE4-C8E3-83BB-9D943D27079E";
	setAttr -s 2 ".ip";
	setAttr ".ip[0].gtg" -type "string" "cluster25";
	setAttr ".ip[1].gtg" -type "string" "cluster25";
	setAttr -s 2 ".og";
	setAttr -s 2 ".orggeom";
	setAttr -s 2 ".wl";
	setAttr ".wl[0:1].w"
		4 1 0.5 2 0.20000000298023224 4 0.20000000298023224 5 
		0.5
		4 1 0.5 2 0.20000000298023224 4 0.20000000298023224 5 
		0.5;
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode blendShape -n "blendShape7";
	rename -uid "70907D64-45A3-7587-5784-9788041C8BE6";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 6;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lip_upper_guide","weight[0]"} ;
createNode blendShape -n "blendShape8";
	rename -uid "2B906B64-4D21-5A1E-19DE-5B9238B601A7";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 7;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lip_lower_guide","weight[0]"} ;
createNode cluster -n "lip_follow_07Cluster";
	rename -uid "78107891-46FA-92A6-9CCF-74BB298D416F";
	setAttr -s 2 ".ip";
	setAttr ".ip[0].gtg" -type "string" "cluster26_1";
	setAttr ".ip[1].gtg" -type "string" "cluster26_1";
	setAttr -s 2 ".og";
	setAttr -s 2 ".orggeom";
	setAttr -s 2 ".wl";
	setAttr ".wl[0:1].w"
		4 1 0.5 2 0.20000000298023224 4 0.20000000298023224 5 
		0.5
		4 1 0.5 2 0.20000000298023224 4 0.20000000298023224 5 
		0.5;
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode blendShape -n "blendShape9";
	rename -uid "48BCA700-4612-6692-4B0F-8C99D1AD62D8";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 8;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lip_upper_guide","weight[0]"} ;
createNode blendShape -n "blendShape10";
	rename -uid "064ADC5D-4E4F-8BA9-FFD2-A185646DBDC3";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 9;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lip_upper_guide","weight[0]"} ;
createNode blendShape -n "blendShape11";
	rename -uid "0D5B60A0-4467-4CC6-9C3E-BAA6C70E9E10";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 10;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lip_lower_guide","weight[0]"} ;
createNode blendShape -n "blendShape12";
	rename -uid "4B80A43B-4C14-E43E-4714-9AAE6922EFBC";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".mlid" 11;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"lip_lower_guide","weight[0]"} ;
createNode cluster -n "lip_follow_06Cluster";
	rename -uid "014FE2D1-4589-1A6A-9BB2-2FA7D9F9AF79";
	setAttr -s 2 ".ip";
	setAttr -s 2 ".og";
	setAttr -s 2 ".orggeom";
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "lip_follow_05Cluster";
	rename -uid "1DDB720C-4E84-67C7-8CBE-2489E567B3ED";
	setAttr -s 2 ".ip";
	setAttr -s 2 ".og";
	setAttr -s 2 ".orggeom";
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode colorMath -n "colorMath1";
	rename -uid "231768C1-492D-A646-BEC4-B698300B07ED";
	setAttr "._cb" -type "float3" -1 -1 -1 ;
	setAttr "._cnd" 2;
createNode multDoubleLinear -n "multDoubleLinear6";
	rename -uid "9F3D704E-41E6-26FA-A269-D697765180C4";
	setAttr ".i2" -1;
createNode colorMath -n "colorMath2";
	rename -uid "2BA67D17-4E4D-FD40-CA4F-1B95C93B4129";
	setAttr "._cb" -type "float3" -1 -1 -1 ;
	setAttr "._cnd" 2;
createNode unitConversion -n "unitConversion3";
	rename -uid "6BA96B42-4812-CEDB-40B3-01B310D8D99F";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion4";
	rename -uid "70FD5AA0-40AC-103C-CFEC-8E98B9D64771";
	setAttr ".cf" 0.017453292519943295;
createNode colorMath -n "colorMath3";
	rename -uid "42C8DF5B-4749-FD6A-B87D-C6B9E51719B2";
	setAttr "._cb" -type "float3" -1 -1 -1 ;
	setAttr "._cnd" 2;
createNode unitConversion -n "unitConversion5";
	rename -uid "043BBDD2-4951-AF9F-0DC6-74B3A2FBC4AF";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion6";
	rename -uid "D211863A-4FA7-44B5-5A2E-619C8BDF688A";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion7";
	rename -uid "04941DD7-4625-23C3-7DAB-3FB3FA15EC26";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion8";
	rename -uid "8F51ED3D-40CC-C9B4-8B53-19952D2A64C9";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion9";
	rename -uid "481CD3B9-4DF5-8AEF-AF8E-3BBE70D6B4DA";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion10";
	rename -uid "AFC31E08-409D-2366-0F6A-11BCFB69A0EC";
	setAttr ".cf" 0.017453292519943295;
createNode colorMath -n "colorMath4";
	rename -uid "012312DC-4950-0516-AF25-D8AAD6C0494A";
	setAttr "._cb" -type "float3" -1 -1 -1 ;
	setAttr "._cnd" 2;
createNode unitConversion -n "unitConversion11";
	rename -uid "A6BB0400-42D0-6E3E-5748-35ACDD01E5DB";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion12";
	rename -uid "A4815312-4E19-BA63-9341-80B0FFFC9335";
	setAttr ".cf" 0.017453292519943295;
createNode multDoubleLinear -n "multDoubleLinear7";
	rename -uid "CE955BB4-49A9-AE64-9783-D29C0C0F5860";
	setAttr ".i2" -1;
createNode colorMath -n "colorMath5";
	rename -uid "1EC190C4-4795-228A-62CE-A4AA4906FEE0";
	setAttr "._cb" -type "float3" -1 -1 -1 ;
	setAttr "._cnd" 2;
createNode unitConversion -n "unitConversion13";
	rename -uid "33E25A8C-4D68-37A8-D720-5AA38F1C331F";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion15";
	rename -uid "756CE19B-406E-F496-E999-B5B1670AEC9C";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion16";
	rename -uid "7D18DA69-422E-50C1-DE91-91B973D78AE9";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion17";
	rename -uid "C300298F-4718-12C3-7CA2-6B80D296E71E";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion18";
	rename -uid "034D4829-453F-3032-068A-208EDCB434C1";
	setAttr ".cf" 0.017453292519943295;
createNode colorMath -n "colorMath6";
	rename -uid "4851E6BC-4E0E-9BAA-86B7-18BBA3029850";
	setAttr "._cb" -type "float3" -1 -1 -1 ;
	setAttr "._cnd" 2;
createNode unitConversion -n "unitConversion19";
	rename -uid "6555CF73-4D73-1E1E-D4C6-039812328F1E";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion20";
	rename -uid "6C51FDD9-43C4-7ADA-7733-09A4CAB0EF94";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion21";
	rename -uid "456EA295-499E-74EA-5CF3-089B36606EB2";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion22";
	rename -uid "51E026A4-4C5E-6FD7-12FB-EBB5A52675D0";
	setAttr ".cf" 0.017453292519943295;
createNode colorMath -n "colorMath7";
	rename -uid "C82D8FA9-4470-E5A2-F3E0-9CA5CB8C70A3";
	setAttr "._cb" -type "float3" -1 -1 -1 ;
	setAttr "._cnd" 2;
createNode unitConversion -n "unitConversion23";
	rename -uid "2197FC47-4C4A-BA96-E2AE-0FAD65BC9E2B";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion24";
	rename -uid "8BAAB63C-43E9-C381-2909-A5BA7947C663";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion25";
	rename -uid "3587D543-4DB9-FC55-1982-EDA6ED3FC245";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion26";
	rename -uid "344C1391-4748-0E53-D07F-8E9ED356843C";
	setAttr ".cf" 0.017453292519943295;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "D804C067-4B14-76D6-33C2-4CAF175CC67B";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2154.1948484077811 -7989.299741511406 ;
	setAttr ".tgi[0].vh" -type "double2" -1239.0688236562066 -7184.2577472855028 ;
createNode RedshiftOptions -s -n "redshiftOptions";
	rename -uid "DF1A032C-4C80-07B7-0FE2-ECA842C5E287";
	setAttr ".version" 3;
	setAttr ".primaryGIEngine" 4;
	setAttr ".secondaryGIEngine" 2;
	setAttr ".numGIBounces" 4;
createNode RedshiftPostEffects -n "defaultRedshiftPostEffects";
	rename -uid "0BB343B8-421B-D54B-B823-DCB29D19DB2B";
	setAttr ".v" 2;
	setAttr -s 2 ".cr[1]" -type "float2" 1 1;
	setAttr -s 2 ".cg[1]" -type "float2" 1 1;
	setAttr -s 2 ".cb[1]" -type "float2" 1 1;
	setAttr -s 2 ".cl[1]" -type "float2" 1 1;
createNode renderSetup -n "renderSetup";
	rename -uid "9BE73DD8-43CC-1BBF-36AA-32B67766023B";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 1;
	setAttr -av ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 15 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -k on ".macc";
	setAttr -k on ".macd";
	setAttr -k on ".macq";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -k on ".gama";
	setAttr -av -k on ".bfs";
	setAttr -k on ".be";
	setAttr -k on ".fec";
	setAttr -k on ".ofc";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -k on ".sp";
	setAttr -k on ".shs";
	setAttr -k on ".lpr";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -av -k on ".mbf";
	setAttr -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -av -k on ".bll";
	setAttr -k on ".bls";
	setAttr -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -k on ".ope";
	setAttr -k on ".oppf";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w";
	setAttr -av ".h";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "C:/Program Files/Autodesk/Maya2022/resources/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".vtn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".vn" -type "string" "ACES 1.0 SDR-video";
	setAttr ".dn" -type "string" "sRGB";
	setAttr ".wsn" -type "string" "ACEScg";
	setAttr ".otn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".potn" -type "string" "ACES 1.0 SDR-video (sRGB)";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -cb on ".hwcc";
	setAttr -cb on ".hwdp";
	setAttr -cb on ".hwql";
	setAttr -k on ".hwfr";
connectAttr "face_guide.s" "face_upper_guide.is";
connectAttr "face_upper_guide.s" "eye_socket_l_guide.is";
connectAttr "noSelect.di" "eye_socket_l_guide.do";
connectAttr "multDoubleLinear7.o" "eye_socket_l_guide.tx";
connectAttr "eye_socket_r_guide.ty" "eye_socket_l_guide.ty";
connectAttr "eye_socket_r_guide.tz" "eye_socket_l_guide.tz";
connectAttr "eye_socket_l_guide.s" "eye_l_guide.is";
connectAttr "noSelect.di" "eye_l_guide.do";
connectAttr "face_upper_guide.s" "eye_socket_r_guide.is";
connectAttr "eye_socket_r_guide.s" "eye_r_guide.is";
connectAttr "face_upper_guide.s" "nose_bridge_guide.is";
connectAttr "nose_bridge_guide.s" "nose_guide.is";
connectAttr "colorMath4.ocr" "sneer_l_guide.tx";
connectAttr "unitConversion12.o" "sneer_l_guide.rx";
connectAttr "sneer_r_guide.rz" "sneer_l_guide.rz";
connectAttr "nose_guide.s" "sneer_l_guide.is";
connectAttr "noSelect.di" "sneer_l_guide.do";
connectAttr "nostril_r_guide.ty" "nostril_l_guide.ty";
connectAttr "sneer_l_guide.s" "nostril_l_guide.is";
connectAttr "noSelect.di" "nostril_l_guide.do";
connectAttr "nose_guide.s" "sneer_r_guide.is";
connectAttr "sneer_r_guide.s" "nostril_r_guide.is";
connectAttr "face_upper_guide.s" "brow_r_guide.is";
connectAttr "brow_r_guide.s" "brow_peak_r_guide.is";
connectAttr "brow_r_guide.s" "brow_inner_r_guide.is";
connectAttr "brow_inner_r_guide.s" "brow_corrugator_r_guide.is";
connectAttr "unitConversion10.o" "brow_l_guide.ry";
connectAttr "unitConversion9.o" "brow_l_guide.rx";
connectAttr "face_upper_guide.s" "brow_l_guide.is";
connectAttr "noSelect.di" "brow_l_guide.do";
connectAttr "brow_r_guide.ty" "brow_l_guide.ty";
connectAttr "brow_r_guide.tz" "brow_l_guide.tz";
connectAttr "colorMath1.ocr" "brow_l_guide.tx";
connectAttr "unitConversion4.o" "brow_peak_l_guide.ry";
connectAttr "brow_l_guide.s" "brow_peak_l_guide.is";
connectAttr "noSelect.di" "brow_peak_l_guide.do";
connectAttr "colorMath2.ocr" "brow_peak_l_guide.tz";
connectAttr "brow_peak_r_guide.tx" "brow_peak_l_guide.tx";
connectAttr "brow_peak_r_guide.ty" "brow_peak_l_guide.ty";
connectAttr "unitConversion6.o" "brow_inner_l_guide.ry";
connectAttr "brow_l_guide.s" "brow_inner_l_guide.is";
connectAttr "noSelect.di" "brow_inner_l_guide.do";
connectAttr "colorMath3.ocr" "brow_inner_l_guide.tz";
connectAttr "brow_inner_r_guide.tx" "brow_inner_l_guide.tx";
connectAttr "brow_inner_r_guide.ty" "brow_inner_l_guide.ty";
connectAttr "brow_corrugator_r_guide.rz" "brow_corrugator_l_guide.rz";
connectAttr "brow_inner_l_guide.s" "brow_corrugator_l_guide.is";
connectAttr "noSelect.di" "brow_corrugator_l_guide.do";
connectAttr "brow_corrugator_r_guide.tx" "brow_corrugator_l_guide.tx";
connectAttr "brow_corrugator_r_guide.ty" "brow_corrugator_l_guide.ty";
connectAttr "multDoubleLinear6.o" "brow_corrugator_l_guide.tz";
connectAttr "face_guide.s" "face_lower_guide.is";
connectAttr "face_lower_guide.s" "jaw_trans_guide.is";
connectAttr "jaw_trans_guide.s" "jaw_guide.is";
connectAttr "jaw_guide.s" "jaw_tip_guide.is";
connectAttr "tongue_01_guide.s" "tongue_02_guide.is";
connectAttr "tongue_02_guide.s" "tongue_03_guide.is";
connectAttr "tongue_03_guide.s" "tongue_04_guide.is";
connectAttr "tongue_04_guide.s" "tongue_05_guide.is";
connectAttr "tongue_05_guide.s" "tongue_06_guide.is";
connectAttr "tongue_06_guide.s" "tongue_07_guide.is";
connectAttr "lid_handle_03Cluster.og[0]" "lid_upper_r_guideCrvShape.cr";
connectAttr "lid_handle_04Cluster.og[0]" "lid_lower_r_guideCrvShape.cr";
connectAttr "lid_handle_10Cluster.og[0]" "lid_mid_r_guideCrvShape.cr";
connectAttr "lip_follow_02Cluster.og[0]" "lip_upper_guideCrvShape.cr";
connectAttr "lip_handle_04Cluster.og[0]" "lip_lower_guideCrvShape.cr";
connectAttr "noSelect.di" "cheek_upper_l_guide.do";
connectAttr "colorMath5.ocr" "cheek_upper_l_guide.tx";
connectAttr "cheek_upper_r_guide.ty" "cheek_upper_l_guide.ty";
connectAttr "cheek_upper_r_guide.tz" "cheek_upper_l_guide.tz";
connectAttr "unitConversion17.o" "cheek_upper_l_guide.rx";
connectAttr "unitConversion18.o" "cheek_upper_l_guide.ry";
connectAttr "cheek_upper_r_guide.rz" "cheek_upper_l_guide.rz";
connectAttr "noSelect.di" "cheek_l_guide.do";
connectAttr "colorMath6.ocr" "cheek_l_guide.tx";
connectAttr "cheek_r_guide.ty" "cheek_l_guide.ty";
connectAttr "cheek_r_guide.tz" "cheek_l_guide.tz";
connectAttr "unitConversion21.o" "cheek_l_guide.rx";
connectAttr "unitConversion22.o" "cheek_l_guide.ry";
connectAttr "cheek_r_guide.rz" "cheek_l_guide.rz";
connectAttr "noSelect.di" "cheek_lower_l_guide.do";
connectAttr "colorMath7.ocr" "cheek_lower_l_guide.tx";
connectAttr "cheek_lower_r_guide.ty" "cheek_lower_l_guide.ty";
connectAttr "cheek_lower_r_guide.tz" "cheek_lower_l_guide.tz";
connectAttr "unitConversion25.o" "cheek_lower_l_guide.rx";
connectAttr "unitConversion26.o" "cheek_lower_l_guide.ry";
connectAttr "cheek_lower_r_guide.rz" "cheek_lower_l_guide.rz";
connectAttr "noSelect.di" "lip_lower_frown_guideCrv.do";
connectAttr "lip_follow_07Cluster.og[0]" "lip_lower_frown_guideCrvShape.cr";
connectAttr "noSelect.di" "lip_upper_frown_guideCrv.do";
connectAttr "lip_follow_07Cluster.og[1]" "lip_upper_frown_guideCrvShape.cr";
connectAttr "noSelect.di" "lip_lower_smile_guideCrv.do";
connectAttr "lip_follow_08Cluster.og[0]" "lip_lower_smile_guideCrvShape.cr";
connectAttr "noSelect.di" "lip_upper_smile_guideCrv.do";
connectAttr "lip_follow_08Cluster.og[1]" "lip_upper_smile_guideCrvShape.cr";
connectAttr "noSelect.di" "lip_lower_wide_guideCrv.do";
connectAttr "lip_follow_05Cluster.og[1]" "lip_lower_wide_guideCrvShape.cr";
connectAttr "noSelect.di" "lip_upper_wide_guideCrv.do";
connectAttr "lip_follow_05Cluster.og[0]" "lip_upper_wide_guideCrvShape.cr";
connectAttr "noSelect.di" "lip_lower_small_guideCrv.do";
connectAttr "lip_follow_06Cluster.og[1]" "lip_lower_small_guideCrvShape.cr";
connectAttr "noSelect.di" "lip_upper_small_guideCrv.do";
connectAttr "lip_follow_06Cluster.og[0]" "lip_upper_small_guideCrvShape.cr";
connectAttr "noSelect.di" "lid_upper_open_r_guideCrv.do";
connectAttr "blendShape1.og[0]" "lid_upper_open_r_guideCrvShape.cr";
connectAttr "noSelect.di" "lid_lower_open_r_guideCrv.do";
connectAttr "blendShape2.og[0]" "lid_lower_open_r_guideCrvShape.cr";
connectAttr "lip_handle_01.ty" "lip_follow_00.ty";
connectAttr "lip_handle_01.tz" "lip_follow_00.tz";
connectAttr "multDoubleLinear1.o" "lip_follow_00.tx";
connectAttr "noSelect.di" "lip_follow_00.do";
connectAttr "lip_handle_02.ty" "lip_follow_01.ty";
connectAttr "lip_handle_02.tz" "lip_follow_01.tz";
connectAttr "multDoubleLinear2.o" "lip_follow_01.tx";
connectAttr "noSelect.di" "lip_follow_01.do";
connectAttr "lip_handle_03.ty" "lip_follow_02.ty";
connectAttr "lip_handle_03.tz" "lip_follow_02.tz";
connectAttr "multDoubleLinear3.o" "lip_follow_02.tx";
connectAttr "noSelect.di" "lip_follow_02.do";
connectAttr "lip_handle_04.ty" "lip_follow_03.ty";
connectAttr "lip_handle_04.tz" "lip_follow_03.tz";
connectAttr "multDoubleLinear4.o" "lip_follow_03.tx";
connectAttr "noSelect.di" "lip_follow_03.do";
connectAttr "multDoubleLinear5.o" "lip_follow_04.tx";
connectAttr "lip_handle_05.ty" "lip_follow_04.ty";
connectAttr "lip_handle_05.tz" "lip_follow_04.tz";
connectAttr "noSelect.di" "lip_follow_04.do";
connectAttr "noSelect.di" "lip_follow_05.do";
connectAttr "noSelect.di" "lip_follow_06.do";
connectAttr "noSelect.di" "lip_follow_07.do";
connectAttr "noSelect.di" "lip_follow_08.do";
connectAttr "tongue_01_bind.s" "tongue_02_bind.is";
connectAttr "tongue_02_bind.s" "tongue_03_bind.is";
connectAttr "tongue_03_bind.s" "tongue_04_bind.is";
connectAttr "tongue_04_bind.s" "tongue_05_bind.is";
connectAttr "tongue_05_bind.s" "tongue_06_bind.is";
connectAttr "tongue_06_bind.s" "tongue_07_bind.is";
connectAttr "face_bind.s" "face_upper_bind.is";
connectAttr "face_upper_bind.s" "eye_socket_l_bind.is";
connectAttr "eye_socket_l_bind.s" "eye_l_bind.is";
connectAttr "face_upper_bind.s" "eye_socket_r_bind.is";
connectAttr "eye_socket_r_bind.s" "eye_r_bind.is";
connectAttr "face_upper_bind.s" "nose_bridge_bind.is";
connectAttr "nose_bridge_bind.s" "nose_bind.is";
connectAttr "nose_bind.s" "sneer_l_bind.is";
connectAttr "sneer_l_bind.s" "nostril_l_bind.is";
connectAttr "nose_bind.s" "sneer_r_bind.is";
connectAttr "sneer_r_bind.s" "nostril_r_bind.is";
connectAttr "face_upper_bind.s" "brow_r_bind.is";
connectAttr "brow_r_bind.s" "brow_peak_r_bind.is";
connectAttr "brow_r_bind.s" "brow_inner_r_bind.is";
connectAttr "brow_inner_r_bind.s" "brow_corrugator_r_bind.is";
connectAttr "face_upper_bind.s" "brow_l_bind.is";
connectAttr "brow_l_bind.s" "brow_peak_l_bind.is";
connectAttr "brow_l_bind.s" "brow_inner_l_bind.is";
connectAttr "brow_inner_l_bind.s" "brow_corrugator_l_bind.is";
connectAttr "face_bind.s" "face_lower_bind.is";
connectAttr "face_lower_bind.s" "jaw_trans_bind.is";
connectAttr "jaw_trans_bind.s" "jaw_bind.is";
connectAttr "jaw_bind.s" "jaw_tip_bind.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "blendShape1.mlpr" "shapeEditorManager.bspr[0]";
connectAttr "blendShape2.mlpr" "shapeEditorManager.bspr[1]";
connectAttr "blendShape3.mlpr" "shapeEditorManager.bspr[2]";
connectAttr "blendShape4.mlpr" "shapeEditorManager.bspr[3]";
connectAttr "blendShape5.mlpr" "shapeEditorManager.bspr[4]";
connectAttr "blendShape6.mlpr" "shapeEditorManager.bspr[5]";
connectAttr "blendShape7.mlpr" "shapeEditorManager.bspr[6]";
connectAttr "blendShape8.mlpr" "shapeEditorManager.bspr[7]";
connectAttr "blendShape9.mlpr" "shapeEditorManager.bspr[8]";
connectAttr "blendShape10.mlpr" "shapeEditorManager.bspr[9]";
connectAttr "blendShape11.mlpr" "shapeEditorManager.bspr[10]";
connectAttr "blendShape12.mlpr" "shapeEditorManager.bspr[11]";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "blendShape3.og[0]" "blendShape1.ip[0].ig";
connectAttr "lid_upper_open_r_guideCrvShapeOrig.l" "blendShape1.orggeom[0]";
connectAttr "shapeEditorManager.obsv[0]" "blendShape1.tgdt[0].dpvs";
connectAttr "lid_mid_r_guideCrvShape.ws" "blendShape1.it[0].itg[0].iti[6000].igt"
		;
connectAttr "blendShape4.og[0]" "blendShape2.ip[0].ig";
connectAttr "lid_lower_open_r_guideCrvShapeOrig.l" "blendShape2.orggeom[0]";
connectAttr "shapeEditorManager.obsv[1]" "blendShape2.tgdt[0].dpvs";
connectAttr "lid_mid_r_guideCrvShape.ws" "blendShape2.it[0].itg[0].iti[6000].igt"
		;
connectAttr "lid_mid_r_guideCrvShapeOrig1.ws" "lid_01_clst.ip[0].ig";
connectAttr "lid_upper_r_guideCrvShapeOrig.ws" "lid_01_clst.ip[1].ig";
connectAttr "lid_lower_r_guideCrvShapeOrig.ws" "lid_01_clst.ip[2].ig";
connectAttr "lid_mid_r_guideCrvShapeOrig1.l" "lid_01_clst.orggeom[0]";
connectAttr "lid_upper_r_guideCrvShapeOrig.l" "lid_01_clst.orggeom[1]";
connectAttr "lid_lower_r_guideCrvShapeOrig.l" "lid_01_clst.orggeom[2]";
connectAttr "lid_handle_00.wm" "lid_01_clst.ma";
connectAttr "lid_handle_00Shape.x" "lid_01_clst.x";
connectAttr "lid_01_clst.og[0]" "lid_handle_07Cluster.ip[0].ig";
connectAttr "lid_01_clst.og[1]" "lid_handle_07Cluster.ip[1].ig";
connectAttr "lid_01_clst.og[2]" "lid_handle_07Cluster.ip[2].ig";
connectAttr "lid_mid_r_guideCrvShapeOrig1.l" "lid_handle_07Cluster.orggeom[0]";
connectAttr "lid_upper_r_guideCrvShapeOrig.l" "lid_handle_07Cluster.orggeom[1]";
connectAttr "lid_lower_r_guideCrvShapeOrig.l" "lid_handle_07Cluster.orggeom[2]";
connectAttr "lid_handle_07.wm" "lid_handle_07Cluster.ma";
connectAttr "lid_handle_07Shape.x" "lid_handle_07Cluster.x";
connectAttr "lid_handle_07Cluster.og[1]" "lid_handle_01Cluster.ip[0].ig";
connectAttr "lid_upper_r_guideCrvShapeOrig.l" "lid_handle_01Cluster.orggeom[0]";
connectAttr "lid_handle_01.wm" "lid_handle_01Cluster.ma";
connectAttr "lid_handle_01Shape.x" "lid_handle_01Cluster.x";
connectAttr "lid_handle_01Cluster.og[0]" "lid_handle_02Cluster.ip[0].ig";
connectAttr "lid_upper_r_guideCrvShapeOrig.l" "lid_handle_02Cluster.orggeom[0]";
connectAttr "lid_handle_02.wm" "lid_handle_02Cluster.ma";
connectAttr "lid_handle_02Shape.x" "lid_handle_02Cluster.x";
connectAttr "lid_handle_02Cluster.og[0]" "lid_handle_03Cluster.ip[0].ig";
connectAttr "lid_upper_r_guideCrvShapeOrig.l" "lid_handle_03Cluster.orggeom[0]";
connectAttr "lid_handle_03.wm" "lid_handle_03Cluster.ma";
connectAttr "lid_handle_03Shape.x" "lid_handle_03Cluster.x";
connectAttr "lid_handle_07Cluster.og[0]" "lid_handle_09Cluster.ip[0].ig";
connectAttr "lid_mid_r_guideCrvShapeOrig1.l" "lid_handle_09Cluster.orggeom[0]";
connectAttr "lid_handle_09.wm" "lid_handle_09Cluster.ma";
connectAttr "lid_handle_09Shape.x" "lid_handle_09Cluster.x";
connectAttr "lid_handle_09Cluster.og[0]" "lid_handle_08Cluster.ip[0].ig";
connectAttr "lid_mid_r_guideCrvShapeOrig1.l" "lid_handle_08Cluster.orggeom[0]";
connectAttr "lid_handle_08.wm" "lid_handle_08Cluster.ma";
connectAttr "lid_handle_08Shape.x" "lid_handle_08Cluster.x";
connectAttr "lid_handle_08Cluster.og[0]" "lid_handle_10Cluster.ip[0].ig";
connectAttr "lid_mid_r_guideCrvShapeOrig1.l" "lid_handle_10Cluster.orggeom[0]";
connectAttr "lid_handle_10.wm" "lid_handle_10Cluster.ma";
connectAttr "lid_handle_10Shape.x" "lid_handle_10Cluster.x";
connectAttr "lid_handle_07Cluster.og[2]" "lid_handle_06Cluster.ip[0].ig";
connectAttr "lid_lower_r_guideCrvShapeOrig.l" "lid_handle_06Cluster.orggeom[0]";
connectAttr "lid_handle_06.wm" "lid_handle_06Cluster.ma";
connectAttr "lid_handle_06Shape.x" "lid_handle_06Cluster.x";
connectAttr "lid_handle_06Cluster.og[0]" "lid_handle_05Cluster.ip[0].ig";
connectAttr "lid_lower_r_guideCrvShapeOrig.l" "lid_handle_05Cluster.orggeom[0]";
connectAttr "lid_handle_05.wm" "lid_handle_05Cluster.ma";
connectAttr "lid_handle_05Shape.x" "lid_handle_05Cluster.x";
connectAttr "lid_handle_05Cluster.og[0]" "lid_handle_04Cluster.ip[0].ig";
connectAttr "lid_lower_r_guideCrvShapeOrig.l" "lid_handle_04Cluster.orggeom[0]";
connectAttr "lid_handle_04.wm" "lid_handle_04Cluster.ma";
connectAttr "lid_handle_04Shape.x" "lid_handle_04Cluster.x";
connectAttr "lip_upper_guideCrvShapeOrig.ws" "lip_handle_03Cluster.ip[0].ig";
connectAttr "lip_lower_guideCrvShapeOrig.ws" "lip_handle_03Cluster.ip[1].ig";
connectAttr "lip_upper_guideCrvShapeOrig.l" "lip_handle_03Cluster.orggeom[0]";
connectAttr "lip_lower_guideCrvShapeOrig.l" "lip_handle_03Cluster.orggeom[1]";
connectAttr "lip_handle_03.wm" "lip_handle_03Cluster.ma";
connectAttr "lip_handle_03Shape.x" "lip_handle_03Cluster.x";
connectAttr "lip_handle_03Cluster.og[0]" "lip_handle_02Cluster.ip[0].ig";
connectAttr "lip_upper_guideCrvShapeOrig.l" "lip_handle_02Cluster.orggeom[0]";
connectAttr "lip_handle_02.wm" "lip_handle_02Cluster.ma";
connectAttr "lip_handle_02Shape.x" "lip_handle_02Cluster.x";
connectAttr "lip_handle_02Cluster.og[0]" "lip_handle_01Cluster.ip[0].ig";
connectAttr "lip_upper_guideCrvShapeOrig.l" "lip_handle_01Cluster.orggeom[0]";
connectAttr "lip_handle_01.wm" "lip_handle_01Cluster.ma";
connectAttr "lip_handle_01Shape.x" "lip_handle_01Cluster.x";
connectAttr "lip_handle_01Cluster.og[0]" "lip_handle_00Cluster.ip[0].ig";
connectAttr "lip_upper_guideCrvShapeOrig.l" "lip_handle_00Cluster.orggeom[0]";
connectAttr "lip_handle_00.wm" "lip_handle_00Cluster.ma";
connectAttr "lip_handle_00Shape.x" "lip_handle_00Cluster.x";
connectAttr "lip_handle_00Cluster.og[0]" "lip_follow_00Cluster.ip[0].ig";
connectAttr "lip_upper_guideCrvShapeOrig.l" "lip_follow_00Cluster.orggeom[0]";
connectAttr "lip_follow_00.wm" "lip_follow_00Cluster.ma";
connectAttr "lip_follow_00Shape.x" "lip_follow_00Cluster.x";
connectAttr "lip_follow_00Cluster.og[0]" "lip_follow_01Cluster.ip[0].ig";
connectAttr "lip_upper_guideCrvShapeOrig.l" "lip_follow_01Cluster.orggeom[0]";
connectAttr "lip_follow_01.wm" "lip_follow_01Cluster.ma";
connectAttr "lip_follow_01Shape.x" "lip_follow_01Cluster.x";
connectAttr "lip_follow_01Cluster.og[0]" "lip_follow_02Cluster.ip[0].ig";
connectAttr "lip_handle_03Cluster.og[1]" "lip_follow_02Cluster.ip[1].ig";
connectAttr "lip_upper_guideCrvShapeOrig.l" "lip_follow_02Cluster.orggeom[0]";
connectAttr "lip_lower_guideCrvShapeOrig.l" "lip_follow_02Cluster.orggeom[1]";
connectAttr "lip_follow_02.wm" "lip_follow_02Cluster.ma";
connectAttr "lip_follow_02Shape.x" "lip_follow_02Cluster.x";
connectAttr "lip_follow_02Cluster.og[1]" "lip_follow_03Cluster.ip[0].ig";
connectAttr "lip_lower_guideCrvShapeOrig.l" "lip_follow_03Cluster.orggeom[0]";
connectAttr "lip_follow_03.wm" "lip_follow_03Cluster.ma";
connectAttr "lip_follow_03Shape.x" "lip_follow_03Cluster.x";
connectAttr "lip_follow_03Cluster.og[0]" "lip_follow_04Cluster.ip[0].ig";
connectAttr "lip_lower_guideCrvShapeOrig.l" "lip_follow_04Cluster.orggeom[0]";
connectAttr "lip_follow_04.wm" "lip_follow_04Cluster.ma";
connectAttr "lip_follow_04Shape.x" "lip_follow_04Cluster.x";
connectAttr "lip_follow_04Cluster.og[0]" "lip_handle_06Cluster.ip[0].ig";
connectAttr "lip_lower_guideCrvShapeOrig.l" "lip_handle_06Cluster.orggeom[0]";
connectAttr "lip_handle_06.wm" "lip_handle_06Cluster.ma";
connectAttr "lip_handle_06Shape.x" "lip_handle_06Cluster.x";
connectAttr "lip_handle_06Cluster.og[0]" "lip_handle_05Cluster.ip[0].ig";
connectAttr "lip_lower_guideCrvShapeOrig.l" "lip_handle_05Cluster.orggeom[0]";
connectAttr "lip_handle_05.wm" "lip_handle_05Cluster.ma";
connectAttr "lip_handle_05Shape.x" "lip_handle_05Cluster.x";
connectAttr "lip_handle_05Cluster.og[0]" "lip_handle_04Cluster.ip[0].ig";
connectAttr "lip_lower_guideCrvShapeOrig.l" "lip_handle_04Cluster.orggeom[0]";
connectAttr "lip_handle_04.wm" "lip_handle_04Cluster.ma";
connectAttr "lip_handle_04Shape.x" "lip_handle_04Cluster.x";
connectAttr "lip_handle_01.tx" "multDoubleLinear1.i1";
connectAttr "lip_handle_02.tx" "multDoubleLinear2.i1";
connectAttr "lip_handle_03.tx" "multDoubleLinear3.i1";
connectAttr "lip_handle_04.tx" "multDoubleLinear4.i1";
connectAttr "lip_handle_05.tx" "multDoubleLinear5.i1";
connectAttr "layerManager.dli[1]" "noSelect.id";
connectAttr "lid_upper_open_r_guideCrvShapeOrig.ws" "blendShape3.ip[0].ig";
connectAttr "lid_upper_open_r_guideCrvShapeOrig.l" "blendShape3.orggeom[0]";
connectAttr "shapeEditorManager.obsv[2]" "blendShape3.tgdt[0].dpvs";
connectAttr "lid_upper_r_guideCrvShape.ws" "blendShape3.it[0].itg[0].iti[6000].igt"
		;
connectAttr "lid_lower_open_r_guideCrvShapeOrig.ws" "blendShape4.ip[0].ig";
connectAttr "lid_lower_open_r_guideCrvShapeOrig.l" "blendShape4.orggeom[0]";
connectAttr "shapeEditorManager.obsv[3]" "blendShape4.tgdt[0].dpvs";
connectAttr "lid_lower_r_guideCrvShape.ws" "blendShape4.it[0].itg[0].iti[6000].igt"
		;
connectAttr "lip_upper_smile_guideCrvShapeOrig1.ws" "blendShape5.ip[0].ig";
connectAttr "lip_upper_smile_guideCrvShapeOrig1.l" "blendShape5.orggeom[0]";
connectAttr "shapeEditorManager.obsv[4]" "blendShape5.tgdt[0].dpvs";
connectAttr "lip_upper_guideCrvShape.ws" "blendShape5.it[0].itg[0].iti[6000].igt"
		;
connectAttr "lip_lower_smile_guideCrvShapeOrig1.ws" "blendShape6.ip[0].ig";
connectAttr "lip_lower_smile_guideCrvShapeOrig1.l" "blendShape6.orggeom[0]";
connectAttr "shapeEditorManager.obsv[5]" "blendShape6.tgdt[0].dpvs";
connectAttr "lip_lower_guideCrvShape.ws" "blendShape6.it[0].itg[0].iti[6000].igt"
		;
connectAttr "blendShape6.og[0]" "lip_follow_08Cluster.ip[0].ig";
connectAttr "blendShape5.og[0]" "lip_follow_08Cluster.ip[1].ig";
connectAttr "lip_lower_smile_guideCrvShapeOrig1.l" "lip_follow_08Cluster.orggeom[0]"
		;
connectAttr "lip_upper_smile_guideCrvShapeOrig1.l" "lip_follow_08Cluster.orggeom[1]"
		;
connectAttr "lip_follow_08.wm" "lip_follow_08Cluster.ma";
connectAttr "lip_follow_08Shape.x" "lip_follow_08Cluster.x";
connectAttr "lip_upper_frown_guideCrvShapeOrig1.ws" "blendShape7.ip[0].ig";
connectAttr "lip_upper_frown_guideCrvShapeOrig1.l" "blendShape7.orggeom[0]";
connectAttr "shapeEditorManager.obsv[6]" "blendShape7.tgdt[0].dpvs";
connectAttr "lip_upper_guideCrvShape.ws" "blendShape7.it[0].itg[0].iti[6000].igt"
		;
connectAttr "lip_lower_frown_guideCrvShapeOrig1.ws" "blendShape8.ip[0].ig";
connectAttr "lip_lower_frown_guideCrvShapeOrig1.l" "blendShape8.orggeom[0]";
connectAttr "shapeEditorManager.obsv[7]" "blendShape8.tgdt[0].dpvs";
connectAttr "lip_lower_guideCrvShape.ws" "blendShape8.it[0].itg[0].iti[6000].igt"
		;
connectAttr "blendShape8.og[0]" "lip_follow_07Cluster.ip[0].ig";
connectAttr "blendShape7.og[0]" "lip_follow_07Cluster.ip[1].ig";
connectAttr "lip_lower_frown_guideCrvShapeOrig1.l" "lip_follow_07Cluster.orggeom[0]"
		;
connectAttr "lip_upper_frown_guideCrvShapeOrig1.l" "lip_follow_07Cluster.orggeom[1]"
		;
connectAttr "lip_follow_07.wm" "lip_follow_07Cluster.ma";
connectAttr "lip_follow_07Shape.x" "lip_follow_07Cluster.x";
connectAttr "lip_upper_small_guideCrvShapeOrig1.ws" "blendShape9.ip[0].ig";
connectAttr "lip_upper_small_guideCrvShapeOrig1.l" "blendShape9.orggeom[0]";
connectAttr "shapeEditorManager.obsv[8]" "blendShape9.tgdt[0].dpvs";
connectAttr "lip_upper_guideCrvShape.ws" "blendShape9.it[0].itg[0].iti[6000].igt"
		;
connectAttr "lip_upper_wide_guideCrvShapeOrig1.ws" "blendShape10.ip[0].ig";
connectAttr "lip_upper_wide_guideCrvShapeOrig1.l" "blendShape10.orggeom[0]";
connectAttr "shapeEditorManager.obsv[9]" "blendShape10.tgdt[0].dpvs";
connectAttr "lip_upper_guideCrvShape.ws" "blendShape10.it[0].itg[0].iti[6000].igt"
		;
connectAttr "lip_lower_small_guideCrvShapeOrig1.ws" "blendShape11.ip[0].ig";
connectAttr "lip_lower_small_guideCrvShapeOrig1.l" "blendShape11.orggeom[0]";
connectAttr "shapeEditorManager.obsv[10]" "blendShape11.tgdt[0].dpvs";
connectAttr "lip_lower_guideCrvShape.ws" "blendShape11.it[0].itg[0].iti[6000].igt"
		;
connectAttr "lip_lower_wide_guideCrvShapeOrig1.ws" "blendShape12.ip[0].ig";
connectAttr "lip_lower_wide_guideCrvShapeOrig1.l" "blendShape12.orggeom[0]";
connectAttr "shapeEditorManager.obsv[11]" "blendShape12.tgdt[0].dpvs";
connectAttr "lip_lower_guideCrvShape.ws" "blendShape12.it[0].itg[0].iti[6000].igt"
		;
connectAttr "blendShape9.og[0]" "lip_follow_06Cluster.ip[0].ig";
connectAttr "blendShape11.og[0]" "lip_follow_06Cluster.ip[1].ig";
connectAttr "lip_upper_small_guideCrvShapeOrig1.l" "lip_follow_06Cluster.orggeom[0]"
		;
connectAttr "lip_lower_small_guideCrvShapeOrig1.l" "lip_follow_06Cluster.orggeom[1]"
		;
connectAttr "lip_follow_06.wm" "lip_follow_06Cluster.ma";
connectAttr "lip_follow_06Shape.x" "lip_follow_06Cluster.x";
connectAttr "blendShape10.og[0]" "lip_follow_05Cluster.ip[0].ig";
connectAttr "blendShape12.og[0]" "lip_follow_05Cluster.ip[1].ig";
connectAttr "lip_upper_wide_guideCrvShapeOrig1.l" "lip_follow_05Cluster.orggeom[0]"
		;
connectAttr "lip_lower_wide_guideCrvShapeOrig1.l" "lip_follow_05Cluster.orggeom[1]"
		;
connectAttr "lip_follow_05.wm" "lip_follow_05Cluster.ma";
connectAttr "lip_follow_05Shape.x" "lip_follow_05Cluster.x";
connectAttr "brow_r_guide.tx" "colorMath1._car";
connectAttr "unitConversion8.o" "colorMath1._cag";
connectAttr "unitConversion7.o" "colorMath1._cab";
connectAttr "brow_corrugator_r_guide.tz" "multDoubleLinear6.i1";
connectAttr "brow_peak_r_guide.tz" "colorMath2._car";
connectAttr "unitConversion3.o" "colorMath2._cag";
connectAttr "brow_peak_r_guide.ry" "unitConversion3.i";
connectAttr "colorMath2.ocg" "unitConversion4.i";
connectAttr "brow_inner_r_guide.tz" "colorMath3._car";
connectAttr "unitConversion5.o" "colorMath3._cag";
connectAttr "brow_inner_r_guide.ry" "unitConversion5.i";
connectAttr "colorMath3.ocg" "unitConversion6.i";
connectAttr "brow_r_guide.ry" "unitConversion7.i";
connectAttr "brow_r_guide.rx" "unitConversion8.i";
connectAttr "colorMath1.ocg" "unitConversion9.i";
connectAttr "colorMath1.ocb" "unitConversion10.i";
connectAttr "sneer_r_guide.tx" "colorMath4._car";
connectAttr "unitConversion11.o" "colorMath4._cag";
connectAttr "sneer_r_guide.rx" "unitConversion11.i";
connectAttr "colorMath4.ocg" "unitConversion12.i";
connectAttr "eye_socket_r_guide.tx" "multDoubleLinear7.i1";
connectAttr "cheek_upper_r_guide.tx" "colorMath5._car";
connectAttr "unitConversion16.o" "colorMath5._cag";
connectAttr "unitConversion15.o" "colorMath5._cab";
connectAttr "cheek_upper_r_guide.rx" "unitConversion13.i";
connectAttr "cheek_upper_r_guide.ry" "unitConversion15.i";
connectAttr "cheek_upper_r_guide.rx" "unitConversion16.i";
connectAttr "colorMath5.ocg" "unitConversion17.i";
connectAttr "colorMath5.ocb" "unitConversion18.i";
connectAttr "cheek_r_guide.tx" "colorMath6._car";
connectAttr "unitConversion19.o" "colorMath6._cag";
connectAttr "unitConversion20.o" "colorMath6._cab";
connectAttr "cheek_r_guide.rx" "unitConversion19.i";
connectAttr "cheek_r_guide.ry" "unitConversion20.i";
connectAttr "colorMath6.ocg" "unitConversion21.i";
connectAttr "colorMath6.ocb" "unitConversion22.i";
connectAttr "cheek_lower_r_guide.tx" "colorMath7._car";
connectAttr "unitConversion23.o" "colorMath7._cag";
connectAttr "unitConversion24.o" "colorMath7._cab";
connectAttr "cheek_lower_r_guide.rx" "unitConversion23.i";
connectAttr "cheek_lower_r_guide.ry" "unitConversion24.i";
connectAttr "colorMath7.ocg" "unitConversion25.i";
connectAttr "colorMath7.ocb" "unitConversion26.i";
connectAttr "defaultRedshiftPostEffects.msg" ":redshiftOptions.postEffects";
connectAttr "multDoubleLinear1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multDoubleLinear2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multDoubleLinear3.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multDoubleLinear4.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multDoubleLinear5.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "colorMath1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multDoubleLinear6.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "colorMath2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "colorMath3.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "colorMath4.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multDoubleLinear7.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "colorMath5.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "colorMath6.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "colorMath7.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRedshiftPostEffects.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of faceSkeleton.ma
