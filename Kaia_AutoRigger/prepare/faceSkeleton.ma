//Maya ASCII 2022 scene
//Name: faceSkeleton.ma
//Last modified: Tue, Sep 13, 2022 01:37:15 AM
//Codeset: 949
requires maya "2022";
requires -nodeType "RedshiftOptions" -nodeType "RedshiftPostEffects" "redshift4maya" "3.0.64";
requires "stereoCamera" "10.0";
requires "mtoa" "4.2.3";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2022";
fileInfo "version" "2022";
fileInfo "cutIdentifier" "202106180615-26a94e7f8c";
fileInfo "osv" "Windows 10 Home v2009 (Build: 19043)";
fileInfo "UUID" "FAAF6747-4613-012F-B6DC-BFB32274CCAD";
createNode transform -s -n "persp";
	rename -uid "D82E65E5-4C47-4946-6543-25BE34AAF9C2";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 11.070310085801474 99.413748679292809 35.472964798873129 ;
	setAttr ".r" -type "double3" -6.9383527256970208 -341.00000000021134 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "0365293B-445B-290E-367B-818C1EBDE253";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 33.567411210470631;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0.0010721392658289697 97.593354007360716 3.8603619406644771 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "FFF62337-4393-2074-5FF2-D88ABB002049";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "C0950844-4EEC-C97D-4B8B-1FBF640AC18D";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "434DD449-4732-4527-4E6C-6FA53E007158";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "F0E50BEB-4AD2-46BE-B326-CD9EE02E2569";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "47A3963D-49E7-E493-F56B-808DC0E1818A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "E85AEC9E-45B7-E51F-E66F-59BA64CE49C4";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "face_guide_Grp";
	rename -uid "C28619B0-4898-324C-E99D-7AAD6712F097";
createNode joint -n "face_bind" -p "face_guide_Grp";
	rename -uid "24A293BD-4EB6-FD8C-EA7C-F4B10CA825A9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 3.3019790515124298e-14 100 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3019790515124298e-14 139.54475402832031 -2 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "face_upper_bind" -p "face_bind";
	rename -uid "7EEC5493-451D-FE98-662D-85A5DC290B90";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -3.1029095486420873e-14 -0.1508558961503752 0.3 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1.0000000000000002 0 7.1309187385013778e-19 141.53578757853617 -1.7 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_upper_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "teeth_upper_bind" -p "face_upper_bind";
	rename -uid "61F70567-421F-2B9C-5682-64BC75C1C817";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.013299210928380489 -1.4629718956825002 6.2562535820716851 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.98052129010354039 0.19641282965653928 0
		 0 -0.19641282965653928 0.98052129010354039 0 0.013299210928380489 138.11293712846211 7.0540576876644634 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "teeth_upper_bind";
	setAttr ".radi" 0.5;
createNode joint -n "eye_socket_l_bind" -p "face_upper_bind";
	rename -uid "DBD54292-42DB-A1A4-AC39-A99BC5996706";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 2.8499724750393103 2.8001025199536542 5.7779692449785465 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.6800000667572021 144.65299987792969 1.9069999456405642 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye_socket";
	setAttr ".liw" yes;
createNode joint -n "eye_l_bind" -p "eye_socket_l_bind";
	rename -uid "D9B192CA-4098-B4F2-503E-F59A79D5848B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.6800000667572035 144.65299987792966 1.9069999456405637 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
	setAttr ".radi" 0.5;
createNode joint -n "eye_socket_r_bind" -p "face_upper_bind";
	rename -uid "F70CDEEB-4795-76E9-6D9A-B5A5BC3507AF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -2.8499724750393103 2.8001025199536542 5.7779692449785465 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 0 -1.2246467991473532e-16 0 0 1 0 0 1.2246467991473532e-16 0 -1 0
		 -3.6800000667572021 144.65299987792969 1.9069999456405642 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye_socket";
	setAttr ".liw" yes;
createNode joint -n "eye_r_bind" -p "eye_socket_r_bind";
	rename -uid "56E55749-4CE5-940B-208F-C083F8151514";
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
	setAttr ".radi" 0.5;
createNode joint -n "nose_bridge_bind" -p "face_upper_bind";
	rename -uid "E5D912E0-4F93-B464-EE7C-AD84ABD54774";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -0.019507717542005941 2.0897177622955496 7.1085410904409621 ;
	setAttr ".r" -type "double3" -25.21596939126098 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99996192306476117 0.0078949694251991553 -0.0037177786916076381 0
		 -0.00872653543077671 0.9046738962540336 -0.42601524505106786 0 -2.1684043449710093e-19 0.42603146702364741 0.90470834477508766 0
		 -0.019507717542005941 143.86306330870656 7.8343620802521761 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nose_brige_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "nose_bind" -p "nose_bridge_bind";
	rename -uid "4088FC3D-4DEE-2A0C-7519-DBA5CA32B4E3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 -1.4284871638423489 0.069240130255094554 ;
	setAttr ".r" -type "double3" 23.235886259255395 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -6.9388939039072284e-18 4.3368086899420177e-18 0
		 6.8533465540116807e-18 0.99940289822345529 -0.034552091435368637 0 -3.6686991162046965e-18 0.034552091435368693 0.99940289822345529 0
		 -5.2041704279304213e-16 141.93141255994448 8.9694147686645316 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nose_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "sneer_l_bind" -p "nose_bind";
	rename -uid "62405AB9-40C6-A357-2CD2-9F9023137D89";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 0.21903214560501724 2.8421709430404007e-14 3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 15.675 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 -6.9388939039072284e-18 4.3368086899420177e-18 0
		 7.5896831226623083e-18 0.95289882536415571 -0.30328835885937405 0 -1.6806017649044133e-18 0.30328835885937411 0.95289882536415571 0
		 0.21903214560501705 141.93141255994448 8.969414768664528 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "sneer";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "nostril_l_bind" -p "sneer_l_bind";
	rename -uid "9CF9C637-46B0-2328-DC34-83A18836E652";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" -0.271000000000027 -0.8709993945264074 0 ;
	setAttr ".r" -type "double3" 0 0 -12.484 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.97635641039468091 0.20598525391636685 -0.065560926245923301 0
		 -0.21616697222566983 0.93036887660185497 -0.29611753337043228 0 -1.6806017649044133e-18 0.30328835885937411 0.95289882536415571 0
		 0.49003214560504404 141.17998936799685 9.4803797250003345 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nostril";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "sneer_r_bind" -p "nose_bind";
	rename -uid "2FFFDA64-4EA6-8ACC-5E40-21AA0107547D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -0.21903214560501724 2.8421709430404007e-14 3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" -15.675 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 2.7074830858901341e-18 -1.2672836472673628e-16 0
		 4.0677231322670454e-17 0.95289953436686914 -0.30328613124144665 0 1.1959080448209269e-16 -0.30328613124144671 -0.95289953436686925 0
		 -0.2190319999999962 141.93111672133057 8.9693909197842583 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "sneer";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "nostril_r_bind" -p "sneer_r_bind";
	rename -uid "1C99F81D-48C8-8836-3D1C-059F49CE3838";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -0.271000000000027 -0.8709993945264074 0 ;
	setAttr ".r" -type "double3" 0 0 -12.484 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.97635641039468091 0.20598540717933672 -0.065560444708500781 0
		 0.21616697222566986 0.93036956884119926 -0.29611535842138892 0 1.1959080448209269e-16 -0.30328613124144671 -0.95289953436686925 0
		 -0.49003200000001745 141.1796923348885 9.480354119496571 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nostril";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_r_bind" -p "face_upper_bind";
	rename -uid "1C30DF08-4BCA-964E-97A3-A08D184AF15E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.4146180152893066 4.0503157350175627 6.7629809498786901 ;
	setAttr ".r" -type "double3" 0 -17 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.8;
	setAttr ".liw" yes;
createNode joint -n "brow_peak_r_bind" -p "brow_r_bind";
	rename -uid "9F56C765-4AD5-D6E7-2C1C-DCA494A7A0F1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 1.4215945517698256 0.4014892578125 0.31068968998799384 ;
	setAttr ".r" -type "double3" 0 -7.999999999999984 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_peak";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_inner_r_bind" -p "brow_r_bind";
	rename -uid "879743D1-448F-4474-8F58-8E9F573C4320";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 3.5580569057404188 0.1350860595703125 0.075983850791793373 ;
	setAttr ".r" -type "double3" 0 17.000000000000011 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 0 0
		 0 0 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_inner";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_corrugator_r_bind" -p "brow_inner_r_bind";
	rename -uid "24C80431-4610-C06C-9864-7FB51D87D49D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -0.58711922168731689 0.4221038818359375 0.048930168151857245 ;
	setAttr ".r" -type "double3" 0 0 14.999999999999998 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -9.5416640443905503e-15 0 ;
	setAttr ".bps" -type "matrix" -0.96592582628906831 -0.25881904510252052 -1.2246467991473532e-16 0
		 -0.25881904510252052 0.96592582628906842 3.0814879110195774e-33 0 1.1829179713786698e-16 3.1696191514317612e-17 -1 0
		 -3.1426379680633545 147.62466326971466 8.3068027496337891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_corrugator";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_l_bind" -p "face_upper_bind";
	rename -uid "B10347F2-4F95-5321-65D2-39973B95D28D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
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
	setAttr ".radi" 0.8;
	setAttr ".liw" yes;
createNode joint -n "brow_peak_l_bind" -p "brow_l_bind";
	rename -uid "1E3BAA3D-447E-39E2-6FF3-45BB96351BB1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 1.4215945517698256 0.4014892578125 -0.31068968998799384 ;
	setAttr ".r" -type "double3" 0 7.999999999999984 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_peak";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_inner_l_bind" -p "brow_l_bind";
	rename -uid "E0AFC1F0-441C-CA5B-2274-A49C4EB139D0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 3.5580569057404188 0.1350860595703125 -0.075983850791793373 ;
	setAttr ".r" -type "double3" 0 -17.000000000000011 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 0 0
		 0 0 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_inner";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_corrugator_l_bind" -p "brow_inner_l_bind";
	rename -uid "BAA19FF8-4FCE-BDF5-A507-77A068462336";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
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
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "face_lower_bind" -p "face_bind";
	rename -uid "F254691B-4073-5A62-D871-8685EF384D48";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -3.1029808578294724e-14 1.2348983868225787 0.23811262572524838 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 142.92154186150913 -1.7 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_lower_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "jaw_trans_bind" -p "face_lower_bind";
	rename -uid "9F922C50-4868-3C8D-9C5A-9291AFB1725B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 -1.6262223533614701 -0.37528104248188243 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 141.29531950814766 -0.89218694903278761 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "jaw_trans_bind";
	setAttr ".radi" 0.5;
createNode joint -n "jaw_bind" -p "jaw_trans_bind";
	rename -uid "988CF44A-4F9A-D032-0998-76980C3EF764";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 2.8421709430404007e-14 7.5495165674510645e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "zyx";
	setAttr ".jo" -type "double3" 6.5376777919745059 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96126169593831889 0.27563735581699911 0
		 0 -0.27563735581699911 0.96126169593831889 0 0 141.29531950814768 -0.89218694903278006 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "jaw_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "jaw_tip_bind" -p "jaw_bind";
	rename -uid "3FD8F5D5-4ED4-E8BB-F541-58843000CAF8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 0 6 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.98052129010354039 0.19641282965653953 0
		 0 -0.19641282965653953 0.98052129010354039 0 0 146.72480613686366 6.7018096387646464 1;
	setAttr ".radi" 0.5;
createNode joint -n "teeth_lower_bind" -p "jaw_bind";
	rename -uid "3336476B-4B77-E34A-58B8-08B328BF0081";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 -1.9727878476642644 5.7539645556875119 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.9805212901035405 0.19641282965653939 0
		 0 -0.19641282965653939 0.9805212901035405 0 0.013299211103944053 138.10891582416616 7.2178271315535767 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "teeth_lower_bind";
	setAttr ".radi" 0.5;
createNode transform -n "tongue_bind_Grp" -p "jaw_bind";
	rename -uid "808C83CB-4A28-006C-6B71-5FAD74BDF763";
	setAttr ".t" -type "double3" -3.9443045261050599e-31 0 0 ;
createNode joint -n "tongue_01_bind" -p "tongue_bind_Grp";
	rename -uid "6A05D2E8-41F4-77B2-4E76-A687AE71B871";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 -2.082244642505259 3.8755687121068991 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.659731207211649 -58.044284493724824 89.690656629895017 ;
	setAttr ".radi" 0.5;
createNode joint -n "tongue_02_bind" -p "tongue_01_bind";
	rename -uid "B2D45A57-4256-2018-5ECF-1FA913EF5163";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.6124703227624384 4.4130449852155439e-15 4.9971018038693095e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.043325316350068269 -0.18838287833144121 -12.46555523627443 ;
	setAttr ".radi" 0.5;
createNode joint -n "tongue_03_bind" -p "tongue_02_bind";
	rename -uid "86932918-4202-61BE-F78F-EF9A1E493E10";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.65907319232506711 7.5447105058028003e-15 -3.4452835548585984e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.00014551855653038924 0.002556308020765508 -6.5161244795551916 ;
	setAttr ".radi" 0.51213660487867185;
createNode joint -n "tongue_04_bind" -p "tongue_03_bind";
	rename -uid "22561F32-4F17-7263-C104-698E1FA9AF34";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.63449551202333865 2.5291854570178403e-15 -4.6430142797957764e-19 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.98775210804452e-05 -0.0020099932944911691 -3.4126630577571069 ;
	setAttr ".radi" 0.5;
createNode joint -n "tongue_05_bind" -p "tongue_04_bind";
	rename -uid "35E6DADA-4957-1049-6FF8-9C860F6E1B9B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.5874599140357244 -1.977606734958324e-14 7.9614261368980907e-19 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.00035490689171974497 0.014237736791363096 -2.662717444288174 ;
	setAttr ".radi" 0.5;
createNode joint -n "tongue_06_bind" -p "tongue_05_bind";
	rename -uid "580E0010-488A-EC8C-22CF-2EB53DDDE499";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.43079789301606392 -4.1111102757965079e-15 -7.9674311689481953e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.0012898873536458767 0.018933565599269068 -4.2577920543636401 ;
	setAttr ".radi" 0.50398460503276088;
createNode joint -n "tongue_07_bind" -p "tongue_06_bind";
	rename -uid "EAF32DD7-4D35-8E4F-E4E0-41BE656A700D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0.38893662555992586 -8.7487573996369602e-15 -2.4104781835788241e-18 ;
	setAttr ".r" -type "double3" 6.1224124612957134e-14 2.4425666030301852e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".radi" 0.50398460503276088;
createNode transform -n "cheek_bind_Grp" -p "face_bind";
	rename -uid "BCF5C2B7-4557-68F2-D143-E89B427D412A";
	setAttr ".t" -type "double3" -3.3019790515124298e-14 0 0 ;
createNode joint -n "cheek_upper_r_bind" -p "cheek_bind_Grp";
	rename -uid "905B3D1D-4FB8-24C5-CEEC-32A69D197EA1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.0088734626770002 0.928619384765625 6.5781286358833313 ;
	setAttr ".r" -type "double3" 10 -25.000000000000004 -9 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.89514963424668026 0.14177777382687393 -0.42261826174069961 0
		 0.081574497416672664 0.98416337441241075 0.1573786956242626 0 0.43823821567641952 0.10640260952567288 -0.89253893528902983 0
		 -5.0194792747497514 141.20631408691409 7.2503585815429732 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_r_bind" -p "cheek_bind_Grp";
	rename -uid "AE0282EA-4898-8F9D-73CA-D492BDED897B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.8409991264343244 -0.26737213134765625 5.706020176410675 ;
	setAttr ".r" -type "double3" 25 -39.99999999999995 -11 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.75197004909461707 0.14616817060531706 -0.64278760968653925 0
		 -0.093731058820309424 0.94149034561144784 0.32374437096706443 0 0.65249945124656117 0.30369523378270435 -0.69427204401488463 0
		 -6.3155222335360017 139.21096395275728 6.1109353515469138 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_lower_r_bind" -p "cheek_bind_Grp";
	rename -uid "A22B6A19-419A-8348-4222-1FB1D5265EB5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -4.2566351890563947 -1.9012451171875 5.7940290570259094 ;
	setAttr ".r" -type "double3" 42.012 -39.952313064542345 -17.685 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.7303514067889878 0.2328743016850463 -0.64214981290665241 0
		 -0.18375779411905063 0.83845213017616316 0.51306052128725987 0 0.65789048914074377 0.49271450660372917 -0.56957222481472602 0
		 -5.3362746238708505 136.67111206054699 5.2705068588257085 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_upper_l_bind" -p "cheek_bind_Grp";
	rename -uid "125BD0F2-4B6F-40C4-053C-87934E4B8D18";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 4.0088734626770695 0.928619384765625 6.5781286358833313 ;
	setAttr ".r" -type "double3" -10 25.000000000000004 -9 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.89514963424668026 0.14177777382687393 -0.42261826174069944 0
		 -0.081574497416672637 0.98416337441241075 0.15737869562426277 0 0.43823821567641935 -0.10640260952567306 0.89253893528903006 0
		 5.0194830894470224 141.20631408691403 7.2503566741943315 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_l_bind" -p "cheek_bind_Grp";
	rename -uid "A09AD6A0-4A11-A638-8FD7-0BBCDBF1B44D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 4.8409991264343937 -0.26737213134765625 5.706020176410675 ;
	setAttr ".r" -type "double3" -25 39.99999999999995 -11 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.75197004909461695 0.14616817060531687 -0.64278760968653892 0
		 0.093731058820309771 0.94149034561144773 0.3237443709670646 0 0.65249945124656084 -0.30369523378270474 0.69427204401488418 0
		 5.8340487480163423 138.73069763183588 6.3339762687682724 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_lower_l_bind" -p "cheek_bind_Grp";
	rename -uid "FC9825DA-487C-A796-2045-30886E29DF8B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 4.256635189056464 -1.9012451171875 5.7940290570259094 ;
	setAttr ".r" -type "double3" -42.012 39.952313064542345 -17.685 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 0.7303514067889878 0.2328743016850465 -0.6421498129066523 0
		 0.18375779411905019 0.83845213017616349 0.51306052128725965 0 0.65789048914074399 -0.49271450660372867 0.56957222481472602 0
		 5.2382864952087518 136.72753906250006 5.2657613754272754 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode transform -n "lid_upper_r_curve" -p "face_guide_Grp";
	rename -uid "454F0F10-45FA-BB60-C86F-A0BE72B6841D";
	setAttr ".ovc" 13;
createNode nurbsCurve -n "lid_upper_r_curveShape" -p "lid_upper_r_curve";
	rename -uid "5BD26841-417A-6D30-CD9D-DE8E192AF816";
	setAttr -k off ".v";
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "lid_upper_r_curveShapeOrig" -p "lid_upper_r_curve";
	rename -uid "42ABE2B1-4126-A268-017F-78B674BEF37A";
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
createNode transform -n "lid_lower_r_curve" -p "face_guide_Grp";
	rename -uid "BD02F64B-4C3B-1A04-41DB-F8B7B4C1858B";
	setAttr ".ovc" 13;
createNode nurbsCurve -n "lid_lower_r_curveShape" -p "lid_lower_r_curve";
	rename -uid "C4736B16-4BBF-7A0A-89A8-6F8AC0BBDB41";
	setAttr -k off ".v";
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "lid_lower_r_curveShapeOrig" -p "lid_lower_r_curve";
	rename -uid "15333848-4573-4CE8-46EB-0A9FE12F8CEF";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".ovc" 13;
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
		-2.870902080215247 143.40175017140305 6.8712303854058892
		-3.8660870710125597 143.05619527497618 6.6350729963638742
		-5.1749410629272461 142.94437582128157 6.2767438888549805
		-6.4804145866618965 143.16136243637132 5.8386219817812224
		-6.983070167784529 143.83236694335938 5.5843982696533203
		

		"gtag" 5
		"cluster20" 1 "cv[0]"
		"cluster21" 1 "cv[1]"
		"cluster22" 1 "cv[2]"
		"cluster23" 1 "cv[3]"
		"cluster24" 1 "cv[4]";
createNode transform -n "lip_upper_curve" -p "face_guide_Grp";
	rename -uid "77AA4A07-43D6-90DD-662B-7D93AE3C8C4B";
createNode nurbsCurve -n "lip_upper_curveShape" -p "lip_upper_curve";
	rename -uid "D3E14AD8-476E-4EE2-BFD8-35A6E0248FFB";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_upper_curveShapeOrig" -p "lip_upper_curve";
	rename -uid "7784DF74-49C1-883D-3DD6-AF9EEEDFFBF2";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 28 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster13";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster14";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster15";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster16";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster17";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster18";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster19";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-2.7997858378838041 138.50695929142404 7.1447222916738085
		-2.1079209217423238 138.76602614030833 7.8599373231271548
		-1.2302596054516262 139.01126053596644 8.5559219348554407
		2.6908743673263464e-19 139.09848104136955 8.9196147073204397
		1.2302596054516262 139.01126053596644 8.5559219348554407
		2.1079209217423238 138.76602614030833 7.8599373231271548
		2.7997858378838041 138.50695929142404 7.1447222916738085
		

		"gtag" 28
		"cluster1" 1 "cv[0]"
		"cluster13" 1 "cv[0]"
		"cluster14" 1 "cv[1]"
		"cluster15" 1 "cv[2]"
		"cluster16" 1 "cv[3]"
		"cluster17" 1 "cv[4]"
		"cluster18" 1 "cv[5]"
		"cluster19" 1 "cv[6]"
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
createNode transform -n "lip_lower_curve" -p "face_guide_Grp";
	rename -uid "411261A9-4209-941B-C4BF-ABB2C02CDC43";
createNode nurbsCurve -n "lip_lower_curveShape" -p "lip_lower_curve";
	rename -uid "E223D75F-4B36-690D-0669-95919B446B5F";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_lower_curveShapeOrig" -p "lip_lower_curve";
	rename -uid "9C8DB5CB-4FA0-3F03-7AB8-F3B806632E7A";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 28 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[1].gtagnm" -type "string" "cluster1_1";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[2].gtagnm" -type "string" "cluster1_2";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[3].gtagnm" -type "string" "cluster1_3";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[4].gtagnm" -type "string" "cluster1_4";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[5].gtagnm" -type "string" "cluster1_5";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[6].gtagnm" -type "string" "cluster1_6";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[7].gtagnm" -type "string" "cluster1_7";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[8].gtagnm" -type "string" "cluster1_8";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[9].gtagnm" -type "string" "cluster1_9";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[10].gtagnm" -type "string" "cluster1_10";
	setAttr ".gtag[10].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[11].gtagnm" -type "string" "cluster1_11";
	setAttr ".gtag[11].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[12].gtagnm" -type "string" "cluster1_12";
	setAttr ".gtag[12].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[13].gtagnm" -type "string" "cluster1_13";
	setAttr ".gtag[13].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[14].gtagnm" -type "string" "cluster1_14";
	setAttr ".gtag[14].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[15].gtagnm" -type "string" "cluster1_15";
	setAttr ".gtag[15].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".gtag[16].gtagnm" -type "string" "cluster1_16";
	setAttr ".gtag[16].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[17].gtagnm" -type "string" "cluster1_17";
	setAttr ".gtag[17].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[18].gtagnm" -type "string" "cluster1_18";
	setAttr ".gtag[18].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[19].gtagnm" -type "string" "cluster1_19";
	setAttr ".gtag[19].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[20].gtagnm" -type "string" "cluster1_20";
	setAttr ".gtag[20].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[21].gtagnm" -type "string" "cluster6";
	setAttr ".gtag[21].gtagcmp" -type "componentList" 1 "cv[0]";
	setAttr ".gtag[22].gtagnm" -type "string" "cluster7";
	setAttr ".gtag[22].gtagcmp" -type "componentList" 1 "cv[1]";
	setAttr ".gtag[23].gtagnm" -type "string" "cluster8";
	setAttr ".gtag[23].gtagcmp" -type "componentList" 1 "cv[2]";
	setAttr ".gtag[24].gtagnm" -type "string" "cluster9";
	setAttr ".gtag[24].gtagcmp" -type "componentList" 1 "cv[3]";
	setAttr ".gtag[25].gtagnm" -type "string" "cluster10";
	setAttr ".gtag[25].gtagcmp" -type "componentList" 1 "cv[4]";
	setAttr ".gtag[26].gtagnm" -type "string" "cluster11";
	setAttr ".gtag[26].gtagcmp" -type "componentList" 1 "cv[5]";
	setAttr ".gtag[27].gtagnm" -type "string" "cluster12";
	setAttr ".gtag[27].gtagcmp" -type "componentList" 1 "cv[6]";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 0.25 0.5 0.75 1 1 1
		7
		-2.7997858378838041 138.50695929142404 7.1447222916738085
		-2.025958298218081 138.24934739943291 7.6930703154175015
		-1.1779081307480253 137.98041384079411 8.1739172240111557
		6.0682292337329006e-18 137.79470685151171 8.4849153009747784
		1.1779081307480253 137.98041384079411 8.1739172240111557
		2.025958298218081 138.24934739943291 7.6930703154175015
		2.7997858378838041 138.50695929142404 7.1447222916738085
		

		"gtag" 28
		"cluster1" 1 "cv[0]"
		"cluster10" 1 "cv[4]"
		"cluster11" 1 "cv[5]"
		"cluster12" 1 "cv[6]"
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
		"cluster6" 1 "cv[0]"
		"cluster7" 1 "cv[1]"
		"cluster8" 1 "cv[2]"
		"cluster9" 1 "cv[3]";
createNode transform -n "temp_clst_Grp" -p "face_guide_Grp";
	rename -uid "A88ACDA9-4466-363E-E089-BABF9B803472";
createNode transform -n "cluster1Handle" -p "temp_clst_Grp";
	rename -uid "06384B27-48B0-3FF6-6060-DAAC3D666387";
	setAttr ".rp" -type "double3" -1.6306558847427368 101.95261383056641 6.0392417907714844 ;
	setAttr ".sp" -type "double3" -1.6306558847427368 101.95261383056641 6.0392417907714844 ;
createNode clusterHandle -n "cluster1HandleShape" -p "cluster1Handle";
	rename -uid "0D721073-42F6-1FFA-0B81-9F8D981A56A7";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.6306558847427368 101.95261383056641 6.0392417907714844 ;
createNode transform -n "cluster2Handle" -p "temp_clst_Grp";
	rename -uid "A2473837-44C2-C811-5F3D-E9BFF02C6990";
	setAttr ".rp" -type "double3" -1.8873145580291748 102.704833984375 6.437647819519043 ;
	setAttr ".sp" -type "double3" -1.8873145580291748 102.704833984375 6.437647819519043 ;
createNode clusterHandle -n "cluster2HandleShape" -p "cluster2Handle";
	rename -uid "5A287242-4B9F-D848-FD60-278E0A4422BD";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.8873145580291748 102.704833984375 6.437647819519043 ;
createNode transform -n "cluster3Handle" -p "temp_clst_Grp";
	rename -uid "12BDCB81-4C35-8724-5B95-E483DFBE631B";
	setAttr ".rp" -type "double3" -3.0241072177886963 103.14756011962891 6.5843791961669922 ;
	setAttr ".sp" -type "double3" -3.0241072177886963 103.14756011962891 6.5843791961669922 ;
createNode clusterHandle -n "cluster3HandleShape" -p "cluster3Handle";
	rename -uid "036EAAE9-495B-8CB0-37D2-54B8E52192FC";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -3.0241072177886963 103.14756011962891 6.5843791961669922 ;
createNode transform -n "cluster4Handle" -p "temp_clst_Grp";
	rename -uid "99D6D456-4DCB-7C89-C256-3584DE1210AA";
	setAttr ".rp" -type "double3" -3.9834420680999756 102.85642242431641 6.0141115188598633 ;
	setAttr ".sp" -type "double3" -3.9834420680999756 102.85642242431641 6.0141115188598633 ;
createNode clusterHandle -n "cluster4HandleShape" -p "cluster4Handle";
	rename -uid "E77238B5-41DB-185F-4167-2E86FB6A5834";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -3.9834420680999756 102.85642242431641 6.0141115188598633 ;
createNode transform -n "cluster5Handle" -p "temp_clst_Grp";
	rename -uid "0C7563F8-4E90-CED2-D074-A2AD8B4DAE96";
	setAttr ".rp" -type "double3" -4.2763590812683105 102.36576080322266 5.4278616905212402 ;
	setAttr ".sp" -type "double3" -4.2763590812683105 102.36576080322266 5.4278616905212402 ;
createNode clusterHandle -n "cluster5HandleShape" -p "cluster5Handle";
	rename -uid "A6E2827B-460C-513A-7BB6-AC9E38B78913";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -4.2763590812683105 102.36576080322266 5.4278616905212402 ;
createNode transform -n "cluster6Handle" -p "temp_clst_Grp";
	rename -uid "59C3B605-4419-F5E6-EFB2-7F85C57F9C71";
	setAttr ".rp" -type "double3" -1.7380028963088989 97.562576293945312 5.7681660652160645 ;
	setAttr ".sp" -type "double3" -1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode clusterHandle -n "cluster6HandleShape" -p "cluster6Handle";
	rename -uid "25DABE8C-47DD-7460-CA2A-34B4C6D0CCD2";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode transform -n "cluster7Handle" -p "temp_clst_Grp";
	rename -uid "1862C125-43C7-3572-D32F-27885684C288";
	setAttr ".rp" -type "double3" -1.2576395273208618 97.402664184570312 6.0243597030639648 ;
	setAttr ".sp" -type "double3" -1.2576395273208618 97.402664184570312 6.0243597030639648 ;
createNode clusterHandle -n "cluster7HandleShape" -p "cluster7Handle";
	rename -uid "D051C50C-4ED2-8D3D-1B19-52BB48C26B23";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.2576395273208618 97.402664184570312 6.0243597030639648 ;
createNode transform -n "cluster8Handle" -p "temp_clst_Grp";
	rename -uid "0B6E38D5-4C22-891F-14F4-B1A63A40B62F";
	setAttr ".rp" -type "double3" -0.73120152950286865 97.2357177734375 6.2578797340393066 ;
	setAttr ".sp" -type "double3" -0.73120152950286865 97.2357177734375 6.2578797340393066 ;
createNode clusterHandle -n "cluster8HandleShape" -p "cluster8Handle";
	rename -uid "0B5EB312-4F10-87F8-4B76-48BABA8FC764";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -0.73120152950286865 97.2357177734375 6.2578797340393066 ;
createNode transform -n "cluster9Handle" -p "temp_clst_Grp";
	rename -uid "718DCDAA-4170-485E-C12E-0992ACD7F19A";
	setAttr ".rp" -type "double3" 3.7669308787297348e-18 97.120437622070312 6.4509358406066895 ;
	setAttr ".sp" -type "double3" 3.7669308787297348e-18 97.120437622070312 6.4509358406066895 ;
createNode clusterHandle -n "cluster9HandleShape" -p "cluster9Handle";
	rename -uid "85513CA9-4027-85F3-9164-CFAD6C555AEC";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 3.7669308787297348e-18 97.120437622070312 6.4509358406066895 ;
createNode transform -n "cluster10Handle" -p "temp_clst_Grp";
	rename -uid "56219E83-4AB3-0190-5BF1-77A7B349DFED";
	setAttr ".rp" -type "double3" 0.73120152950286865 97.2357177734375 6.2578797340393066 ;
	setAttr ".sp" -type "double3" 0.73120152950286865 97.2357177734375 6.2578797340393066 ;
createNode clusterHandle -n "cluster10HandleShape" -p "cluster10Handle";
	rename -uid "057F3886-4FE3-ED41-E78F-ACA8F4113B97";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0.73120152950286865 97.2357177734375 6.2578797340393066 ;
createNode transform -n "cluster11Handle" -p "temp_clst_Grp";
	rename -uid "00353933-4E4B-8F06-D722-C88CB2AEEE35";
	setAttr ".rp" -type "double3" 1.2576395273208618 97.402664184570312 6.0243597030639648 ;
	setAttr ".sp" -type "double3" 1.2576395273208618 97.402664184570312 6.0243597030639648 ;
createNode clusterHandle -n "cluster11HandleShape" -p "cluster11Handle";
	rename -uid "52D3D3B6-4932-65BC-802D-2C8711E0C8F8";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.2576395273208618 97.402664184570312 6.0243597030639648 ;
createNode transform -n "cluster12Handle" -p "temp_clst_Grp";
	rename -uid "D2210C84-44EB-974B-6D9D-0E9195DC3431";
	setAttr ".rp" -type "double3" 1.7380028963088989 97.562576293945312 5.7681660652160645 ;
	setAttr ".sp" -type "double3" 1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode clusterHandle -n "cluster12HandleShape" -p "cluster12Handle";
	rename -uid "03562A5C-4E21-D4D1-7F72-3987FF0D2BB4";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode transform -n "cluster13Handle" -p "temp_clst_Grp";
	rename -uid "D75C79BA-4330-3A48-05DD-E4AFCCEB4F48";
	setAttr ".rp" -type "double3" -1.7380028963088989 97.562576293945312 5.7681660652160645 ;
	setAttr ".sp" -type "double3" -1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode clusterHandle -n "cluster13HandleShape" -p "cluster13Handle";
	rename -uid "57384F20-4091-51B7-E25E-CDB7B38DBFF5";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode transform -n "cluster14Handle" -p "temp_clst_Grp";
	rename -uid "E51EAF03-414F-C3E4-5A6D-2688A77AE6CB";
	setAttr ".rp" -type "double3" -1.3085188865661621 97.723396301269531 6.1240477561950684 ;
	setAttr ".sp" -type "double3" -1.3085188865661621 97.723396301269531 6.1240477561950684 ;
createNode clusterHandle -n "cluster14HandleShape" -p "cluster14Handle";
	rename -uid "A2BBDC09-40AF-DBC2-982C-3C809D49FFBC";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.3085188865661621 97.723396301269531 6.1240477561950684 ;
createNode transform -n "cluster15Handle" -p "temp_clst_Grp";
	rename -uid "158346FD-4B1B-A257-7945-E79E75DFF16E";
	setAttr ".rp" -type "double3" -0.76369941234588623 97.875625610351562 6.4950141906738281 ;
	setAttr ".sp" -type "double3" -0.76369941234588623 97.875625610351562 6.4950141906738281 ;
createNode clusterHandle -n "cluster15HandleShape" -p "cluster15Handle";
	rename -uid "26E33F44-4A66-05BD-9B51-FBB12D8A95FC";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -0.76369941234588623 97.875625610351562 6.4950141906738281 ;
createNode transform -n "cluster16Handle" -p "temp_clst_Grp";
	rename -uid "1C81ECEB-4F8A-E3DB-42AC-F2828E75BB8F";
	setAttr ".rp" -type "double3" 1.670394699563718e-19 97.929771423339844 6.7207808494567871 ;
	setAttr ".sp" -type "double3" 1.670394699563718e-19 97.929771423339844 6.7207808494567871 ;
createNode clusterHandle -n "cluster16HandleShape" -p "cluster16Handle";
	rename -uid "5DB8555A-4AF9-BF2E-C50B-32AD94912A3E";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.670394699563718e-19 97.929771423339844 6.7207808494567871 ;
createNode transform -n "cluster17Handle" -p "temp_clst_Grp";
	rename -uid "8AA037B2-412C-38B5-0135-02981B777DE4";
	setAttr ".rp" -type "double3" 0.76369941234588623 97.875625610351562 6.4950141906738281 ;
	setAttr ".sp" -type "double3" 0.76369941234588623 97.875625610351562 6.4950141906738281 ;
createNode clusterHandle -n "cluster17HandleShape" -p "cluster17Handle";
	rename -uid "39831E39-4ECD-039B-33F4-2590C25F5E0E";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0.76369941234588623 97.875625610351562 6.4950141906738281 ;
createNode transform -n "cluster18Handle" -p "temp_clst_Grp";
	rename -uid "5B970237-4849-7E3D-23E8-D09535D2CAAD";
	setAttr ".rp" -type "double3" 1.3085188865661621 97.723396301269531 6.1240477561950684 ;
	setAttr ".sp" -type "double3" 1.3085188865661621 97.723396301269531 6.1240477561950684 ;
createNode clusterHandle -n "cluster18HandleShape" -p "cluster18Handle";
	rename -uid "0C0EC83E-45E6-2264-F856-D6AF3F080738";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.3085188865661621 97.723396301269531 6.1240477561950684 ;
createNode transform -n "cluster19Handle" -p "temp_clst_Grp";
	rename -uid "191414FA-449B-70B0-1027-5CBA1BCCCCE7";
	setAttr ".rp" -type "double3" 1.7380028963088989 97.562576293945312 5.7681660652160645 ;
	setAttr ".sp" -type "double3" 1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode clusterHandle -n "cluster19HandleShape" -p "cluster19Handle";
	rename -uid "C3DF1BFD-438E-11BF-73C4-87A8DA8EAE8A";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.7380028963088989 97.562576293945312 5.7681660652160645 ;
createNode transform -n "cluster20Handle" -p "temp_clst_Grp";
	rename -uid "E5D0C0D3-4836-FBAE-F26C-5A84E44F2328";
	setAttr ".rp" -type "double3" -1.6306558847427368 101.95261383056641 6.0392417907714844 ;
	setAttr ".sp" -type "double3" -1.6306558847427368 101.95261383056641 6.0392417907714844 ;
createNode clusterHandle -n "cluster20HandleShape" -p "cluster20Handle";
	rename -uid "A3218B6F-4330-7E57-7B76-268FEE71DD2B";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -1.6306558847427368 101.95261383056641 6.0392417907714844 ;
createNode transform -n "cluster21Handle" -p "temp_clst_Grp";
	rename -uid "8BB0C90A-4BEB-D30E-5568-2581B196BFF8";
	setAttr ".rp" -type "double3" -2.2685830593109131 101.83708953857422 6.249478816986084 ;
	setAttr ".sp" -type "double3" -2.2685830593109131 101.83708953857422 6.249478816986084 ;
createNode clusterHandle -n "cluster21HandleShape" -p "cluster21Handle";
	rename -uid "D6B9A7DB-42F4-48D2-9B57-6BA1361FC17B";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -2.2685830593109131 101.83708953857422 6.249478816986084 ;
createNode transform -n "cluster22Handle" -p "temp_clst_Grp";
	rename -uid "C68D1782-4378-0D48-3EF0-B08C84430543";
	setAttr ".rp" -type "double3" -3.1095688343048096 101.70172119140625 6.290215015411377 ;
	setAttr ".sp" -type "double3" -3.1095688343048096 101.70172119140625 6.290215015411377 ;
createNode clusterHandle -n "cluster22HandleShape" -p "cluster22Handle";
	rename -uid "1E734D46-48A6-DC69-7442-CBB64FE9FB52";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -3.1095688343048096 101.70172119140625 6.290215015411377 ;
createNode transform -n "cluster23Handle" -p "temp_clst_Grp";
	rename -uid "A70C1174-4DD2-F5DD-CD6C-BCAD17759457";
	setAttr ".rp" -type "double3" -4.0393743515014648 101.97177886962891 5.8298721313476562 ;
	setAttr ".sp" -type "double3" -4.0393743515014648 101.97177886962891 5.8298721313476562 ;
createNode clusterHandle -n "cluster23HandleShape" -p "cluster23Handle";
	rename -uid "F019C84B-4B0B-BED4-72EC-4AB49D53ED2F";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -4.0393743515014648 101.97177886962891 5.8298721313476562 ;
createNode transform -n "cluster24Handle" -p "temp_clst_Grp";
	rename -uid "A066DB8E-4DFB-35C3-AD7F-FEA1E463E792";
	setAttr ".rp" -type "double3" -4.2763590812683105 102.36576080322266 5.4278616905212402 ;
	setAttr ".sp" -type "double3" -4.2763590812683105 102.36576080322266 5.4278616905212402 ;
createNode clusterHandle -n "cluster24HandleShape" -p "cluster24Handle";
	rename -uid "F7B51AEF-480E-F18C-7A06-6B9B3727FC39";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -4.2763590812683105 102.36576080322266 5.4278616905212402 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "D694B79D-48DF-C24E-BE33-749F5FC2D926";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode RedshiftOptions -s -n "redshiftOptions";
	rename -uid "A6F5203E-419B-4734-68C0-45A949D0216C";
	setAttr ".version" 3;
	setAttr ".unifiedFilterSize" 2.5;
	setAttr ".denoiseEngine" 3;
	setAttr ".GIEnabled" yes;
	setAttr ".primaryGIEngine" 4;
	setAttr ".secondaryGIEngine" 2;
	setAttr ".numGIBounces" 4;
	setAttr ".enableLegacyBlackBodyAndDispersionTechnique" no;
	setAttr ".enableOptiXRTOnSupportedGPUs" yes;
	setAttr ".enableAutomaticSampling" yes;
createNode RedshiftPostEffects -n "defaultRedshiftPostEffects";
	rename -uid "9AFCE011-4A73-3986-9186-3495F5640462";
	setAttr ".v" 2;
	setAttr -s 2 ".cr[1]" -type "float2" 1 1;
	setAttr -s 2 ".cg[1]" -type "float2" 1 1;
	setAttr -s 2 ".cb[1]" -type "float2" 1 1;
	setAttr -s 2 ".cl[1]" -type "float2" 1 1;
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "88660EDD-4AD6-7DE0-DA0E-4CA3A416F68F";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "E0E6020C-478D-D7E9-53C6-1FB8560BF241";
createNode displayLayerManager -n "layerManager";
	rename -uid "7CC4884B-43C4-67B4-048E-A3B8DDCC2457";
createNode displayLayer -n "defaultLayer";
	rename -uid "CD90B0CD-41FB-C9C5-89C6-DF92BC3B2AFB";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "E1FE1DFB-4075-BD59-8978-DBB4C1C29197";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "D3F692CF-4E7E-D3F7-08D2-2FA44982A031";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "09FBCD70-47BA-7572-5332-ABB06E9EA3DE";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|top|topShape\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|side|sideShape\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 1\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|front|frontShape\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n"
		+ "            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n"
		+ "            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n"
		+ "            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|persp|perspShape\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n"
		+ "            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n"
		+ "            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n"
		+ "            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1059\n            -height 734\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n"
		+ "            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n"
		+ "            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n"
		+ "            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n"
		+ "            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n"
		+ "                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n"
		+ "                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -keyMinScale 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 0\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n"
		+ "            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n"
		+ "                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n"
		+ "                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n"
		+ "                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n"
		+ "                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n"
		+ "                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n"
		+ "\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"|persp|perspShape\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n"
		+ "                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n"
		+ "                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n"
		+ "                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n"
		+ "                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1059\\n    -height 734\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1059\\n    -height 734\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 50 -size 100 -divisions 3 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "2895A3EC-41BB-018A-A872-758E37F9EEE6";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode cluster -n "cluster1";
	rename -uid "0D019851-4E54-A8DD-2983-3592E4D628D3";
	setAttr ".ip[0].gtg" -type "string" "cluster1";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak1";
	rename -uid "25894A92-47F7-78C9-27AA-62B86EEB28BF";
	setAttr -s 5 ".pl[0].cp[0:4]" -type "double3" 1.2402462397843785 
		-41.449137304070248 -0.83198859463440478 1.0399481948964675 -42.417961206390359 -0.3794690969841783 
		1.9632639393724971 -42.816540572921554 -0.22869726897096854 2.9215891411452444 -42.161849538454362 
		0.19754617314080836 2.7067110865162185 -41.46660879850883 -0.15653657913208008;
createNode cluster -n "cluster2";
	rename -uid "29D4E159-458C-6063-224A-6591B9C34288";
	setAttr ".ip[0].gtg" -type "string" "cluster2";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster3";
	rename -uid "B37175E8-4259-7DDE-0076-1AB3D09AA062";
	setAttr ".ip[0].gtg" -type "string" "cluster3";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster4";
	rename -uid "EF8DE702-45FF-18F1-6255-5897DABADE76";
	setAttr ".ip[0].gtg" -type "string" "cluster4";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster5";
	rename -uid "A2718CBF-4C1E-AC0F-38A6-7FA3760A89A6";
	setAttr ".ip[0].gtg" -type "string" "cluster5";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster6";
	rename -uid "72B20E53-49E8-10C0-DA60-39A063804169";
	setAttr ".ip[0].gtg" -type "string" "cluster6";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak2";
	rename -uid "1EC238EF-4169-73FD-2B6A-87A79ABB17F9";
	setAttr -s 7 ".pl[0].cp[0:6]" -type "double3" 1.0617829436067283 
		-40.944382034219814 -1.3765564151411551 0.76831875367023938 -40.846686021444455 -1.6687104746461445 
		0.44670658213960213 -40.744696411502716 -1.916037585050864 -2.3012982675643901e-18 
		-40.674269412744238 -2.0339796251692084 -0.44670658213960213 -40.744696411502716 
		-1.916037585050864 -0.76831875367023938 -40.846686021444455 -1.6687104746461445 -1.0617829436067283 
		-40.944382034219814 -1.3765564151411551;
createNode cluster -n "cluster7";
	rename -uid "29A64912-4DC2-6BA8-8907-5B8F1C1CB585";
	setAttr ".ip[0].gtg" -type "string" "cluster7";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster8";
	rename -uid "95527AAC-4F98-650E-3C6D-23810CC2F4CD";
	setAttr ".ip[0].gtg" -type "string" "cluster8";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster9";
	rename -uid "191B9DF4-447E-A5E6-18DB-F5A0F6616082";
	setAttr ".ip[0].gtg" -type "string" "cluster9";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster10";
	rename -uid "09DCD53B-4509-AEC7-2FEE-49A9BB95F3EE";
	setAttr ".ip[0].gtg" -type "string" "cluster10";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster11";
	rename -uid "23806E4D-4DB0-F780-FC55-5EB9095B76C7";
	setAttr ".ip[0].gtg" -type "string" "cluster11";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster12";
	rename -uid "71AA7429-4191-C58B-0732-B78D30970793";
	setAttr ".ip[0].gtg" -type "string" "cluster12";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster13";
	rename -uid "921035F1-4F86-55BD-D88F-C7BC9E8FF19F";
	setAttr ".ip[0].gtg" -type "string" "cluster13";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak3";
	rename -uid "B95C67D8-476F-D91F-8044-8595638BEFA4";
	setAttr -s 7 ".pl[0].cp[0:6]" -type "double3" 1.0617829436067283 
		-40.944382034219814 -1.3765564151411551 0.79940202957432716 -41.042629820774607 -1.7358895274437103 
		0.46656020885662208 -41.135631826489558 -2.0609079822304048 -1.0204796623927474e-19 
		-41.168709086798785 -2.1988338111603261 -0.46656020885662208 -41.135631826489558 
		-2.0609079822304048 -0.79940202957432716 -41.042629820774607 -1.7358895274437103 
		-1.0617829436067283 -40.944382034219814 -1.3765564151411551;
createNode cluster -n "cluster14";
	rename -uid "7041A23A-495E-6A08-A732-69A7A38AD877";
	setAttr ".ip[0].gtg" -type "string" "cluster14";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster15";
	rename -uid "E7B530E1-4EA3-5F79-3C90-3C81E765C4C2";
	setAttr ".ip[0].gtg" -type "string" "cluster15";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster16";
	rename -uid "62D7615C-4FA4-1DB6-431F-79ADFAD9EA57";
	setAttr ".ip[0].gtg" -type "string" "cluster16";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster17";
	rename -uid "4EEAFA06-460F-55AF-0A36-9D9F1B58A5EE";
	setAttr ".ip[0].gtg" -type "string" "cluster17";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster18";
	rename -uid "C386C800-4B75-72BF-553E-C8929630F222";
	setAttr ".ip[0].gtg" -type "string" "cluster18";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster19";
	rename -uid "2E218C85-4DA1-62B6-B2F5-FEA2C3CF7636";
	setAttr ".ip[0].gtg" -type "string" "cluster19";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster20";
	rename -uid "26C98050-4E71-85C4-91BD-688B5BD940DD";
	setAttr ".ip[0].gtg" -type "string" "cluster20";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak4";
	rename -uid "C253DB51-4515-AC6E-64E7-938A2AA2E8F0";
	setAttr -s 5 ".pl[0].cp[0:4]" -type "double3" 1.2402462397843785 
		-41.449137304070248 -0.83198859463440478 1.5975040537085978 -41.219102828646001 -0.38559402791676067 
		2.0653721460401675 -41.242654475144036 0.013471265233731877 2.4410400970375417 -41.189581355702458 
		-0.0087499047505046335 2.7067110865162185 -41.46660879850883 -0.15653657913208008;
createNode cluster -n "cluster21";
	rename -uid "31C42CAC-4A9A-5A31-CF31-5DA3D0C3CFFD";
	setAttr ".ip[0].gtg" -type "string" "cluster21";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster22";
	rename -uid "E6755DD5-4A48-7107-5F01-91BB2BD49CCB";
	setAttr ".ip[0].gtg" -type "string" "cluster22";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster23";
	rename -uid "22E6C864-45E5-7E1B-88EC-DB91DBDAA99B";
	setAttr ".ip[0].gtg" -type "string" "cluster23";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode cluster -n "cluster24";
	rename -uid "8BC96891-42B5-AA6A-BA80-5E88DC5D9CC2";
	setAttr ".ip[0].gtg" -type "string" "cluster24";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
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
connectAttr "face_bind.s" "face_upper_bind.is";
connectAttr "face_upper_bind.s" "teeth_upper_bind.is";
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
connectAttr "jaw_bind.s" "teeth_lower_bind.is";
connectAttr "tongue_01_bind.s" "tongue_02_bind.is";
connectAttr "tongue_02_bind.s" "tongue_03_bind.is";
connectAttr "tongue_03_bind.s" "tongue_04_bind.is";
connectAttr "tongue_04_bind.s" "tongue_05_bind.is";
connectAttr "tongue_05_bind.s" "tongue_06_bind.is";
connectAttr "tongue_06_bind.s" "tongue_07_bind.is";
connectAttr "cluster5.og[0]" "lid_upper_r_curveShape.cr";
connectAttr "tweak1.pl[0].cp[0]" "lid_upper_r_curveShape.twl";
connectAttr "cluster24.og[0]" "lid_lower_r_curveShape.cr";
connectAttr "tweak4.pl[0].cp[0]" "lid_lower_r_curveShape.twl";
connectAttr "cluster19.og[0]" "lip_upper_curveShape.cr";
connectAttr "tweak3.pl[0].cp[0]" "lip_upper_curveShape.twl";
connectAttr "cluster12.og[0]" "lip_lower_curveShape.cr";
connectAttr "tweak2.pl[0].cp[0]" "lip_lower_curveShape.twl";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "defaultRedshiftPostEffects.msg" ":redshiftOptions.postEffects";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "tweak1.og[0]" "cluster1.ip[0].ig";
connectAttr "lid_upper_r_curveShapeOrig.l" "cluster1.orggeom[0]";
connectAttr "cluster1Handle.wm" "cluster1.ma";
connectAttr "cluster1HandleShape.x" "cluster1.x";
connectAttr "lid_upper_r_curveShapeOrig.ws" "tweak1.ip[0].ig";
connectAttr "cluster1.og[0]" "cluster2.ip[0].ig";
connectAttr "lid_upper_r_curveShapeOrig.l" "cluster2.orggeom[0]";
connectAttr "cluster2Handle.wm" "cluster2.ma";
connectAttr "cluster2HandleShape.x" "cluster2.x";
connectAttr "cluster2.og[0]" "cluster3.ip[0].ig";
connectAttr "lid_upper_r_curveShapeOrig.l" "cluster3.orggeom[0]";
connectAttr "cluster3Handle.wm" "cluster3.ma";
connectAttr "cluster3HandleShape.x" "cluster3.x";
connectAttr "cluster3.og[0]" "cluster4.ip[0].ig";
connectAttr "lid_upper_r_curveShapeOrig.l" "cluster4.orggeom[0]";
connectAttr "cluster4Handle.wm" "cluster4.ma";
connectAttr "cluster4HandleShape.x" "cluster4.x";
connectAttr "cluster4.og[0]" "cluster5.ip[0].ig";
connectAttr "lid_upper_r_curveShapeOrig.l" "cluster5.orggeom[0]";
connectAttr "cluster5Handle.wm" "cluster5.ma";
connectAttr "cluster5HandleShape.x" "cluster5.x";
connectAttr "tweak2.og[0]" "cluster6.ip[0].ig";
connectAttr "lip_lower_curveShapeOrig.l" "cluster6.orggeom[0]";
connectAttr "cluster6Handle.wm" "cluster6.ma";
connectAttr "cluster6HandleShape.x" "cluster6.x";
connectAttr "lip_lower_curveShapeOrig.ws" "tweak2.ip[0].ig";
connectAttr "cluster6.og[0]" "cluster7.ip[0].ig";
connectAttr "lip_lower_curveShapeOrig.l" "cluster7.orggeom[0]";
connectAttr "cluster7Handle.wm" "cluster7.ma";
connectAttr "cluster7HandleShape.x" "cluster7.x";
connectAttr "cluster7.og[0]" "cluster8.ip[0].ig";
connectAttr "lip_lower_curveShapeOrig.l" "cluster8.orggeom[0]";
connectAttr "cluster8Handle.wm" "cluster8.ma";
connectAttr "cluster8HandleShape.x" "cluster8.x";
connectAttr "cluster8.og[0]" "cluster9.ip[0].ig";
connectAttr "lip_lower_curveShapeOrig.l" "cluster9.orggeom[0]";
connectAttr "cluster9Handle.wm" "cluster9.ma";
connectAttr "cluster9HandleShape.x" "cluster9.x";
connectAttr "cluster9.og[0]" "cluster10.ip[0].ig";
connectAttr "lip_lower_curveShapeOrig.l" "cluster10.orggeom[0]";
connectAttr "cluster10Handle.wm" "cluster10.ma";
connectAttr "cluster10HandleShape.x" "cluster10.x";
connectAttr "cluster10.og[0]" "cluster11.ip[0].ig";
connectAttr "lip_lower_curveShapeOrig.l" "cluster11.orggeom[0]";
connectAttr "cluster11Handle.wm" "cluster11.ma";
connectAttr "cluster11HandleShape.x" "cluster11.x";
connectAttr "cluster11.og[0]" "cluster12.ip[0].ig";
connectAttr "lip_lower_curveShapeOrig.l" "cluster12.orggeom[0]";
connectAttr "cluster12Handle.wm" "cluster12.ma";
connectAttr "cluster12HandleShape.x" "cluster12.x";
connectAttr "tweak3.og[0]" "cluster13.ip[0].ig";
connectAttr "lip_upper_curveShapeOrig.l" "cluster13.orggeom[0]";
connectAttr "cluster13Handle.wm" "cluster13.ma";
connectAttr "cluster13HandleShape.x" "cluster13.x";
connectAttr "lip_upper_curveShapeOrig.ws" "tweak3.ip[0].ig";
connectAttr "cluster13.og[0]" "cluster14.ip[0].ig";
connectAttr "lip_upper_curveShapeOrig.l" "cluster14.orggeom[0]";
connectAttr "cluster14Handle.wm" "cluster14.ma";
connectAttr "cluster14HandleShape.x" "cluster14.x";
connectAttr "cluster14.og[0]" "cluster15.ip[0].ig";
connectAttr "lip_upper_curveShapeOrig.l" "cluster15.orggeom[0]";
connectAttr "cluster15Handle.wm" "cluster15.ma";
connectAttr "cluster15HandleShape.x" "cluster15.x";
connectAttr "cluster15.og[0]" "cluster16.ip[0].ig";
connectAttr "lip_upper_curveShapeOrig.l" "cluster16.orggeom[0]";
connectAttr "cluster16Handle.wm" "cluster16.ma";
connectAttr "cluster16HandleShape.x" "cluster16.x";
connectAttr "cluster16.og[0]" "cluster17.ip[0].ig";
connectAttr "lip_upper_curveShapeOrig.l" "cluster17.orggeom[0]";
connectAttr "cluster17Handle.wm" "cluster17.ma";
connectAttr "cluster17HandleShape.x" "cluster17.x";
connectAttr "cluster17.og[0]" "cluster18.ip[0].ig";
connectAttr "lip_upper_curveShapeOrig.l" "cluster18.orggeom[0]";
connectAttr "cluster18Handle.wm" "cluster18.ma";
connectAttr "cluster18HandleShape.x" "cluster18.x";
connectAttr "cluster18.og[0]" "cluster19.ip[0].ig";
connectAttr "lip_upper_curveShapeOrig.l" "cluster19.orggeom[0]";
connectAttr "cluster19Handle.wm" "cluster19.ma";
connectAttr "cluster19HandleShape.x" "cluster19.x";
connectAttr "tweak4.og[0]" "cluster20.ip[0].ig";
connectAttr "lid_lower_r_curveShapeOrig.l" "cluster20.orggeom[0]";
connectAttr "cluster20Handle.wm" "cluster20.ma";
connectAttr "cluster20HandleShape.x" "cluster20.x";
connectAttr "lid_lower_r_curveShapeOrig.ws" "tweak4.ip[0].ig";
connectAttr "cluster20.og[0]" "cluster21.ip[0].ig";
connectAttr "lid_lower_r_curveShapeOrig.l" "cluster21.orggeom[0]";
connectAttr "cluster21Handle.wm" "cluster21.ma";
connectAttr "cluster21HandleShape.x" "cluster21.x";
connectAttr "cluster21.og[0]" "cluster22.ip[0].ig";
connectAttr "lid_lower_r_curveShapeOrig.l" "cluster22.orggeom[0]";
connectAttr "cluster22Handle.wm" "cluster22.ma";
connectAttr "cluster22HandleShape.x" "cluster22.x";
connectAttr "cluster22.og[0]" "cluster23.ip[0].ig";
connectAttr "lid_lower_r_curveShapeOrig.l" "cluster23.orggeom[0]";
connectAttr "cluster23Handle.wm" "cluster23.ma";
connectAttr "cluster23HandleShape.x" "cluster23.x";
connectAttr "cluster23.og[0]" "cluster24.ip[0].ig";
connectAttr "lid_lower_r_curveShapeOrig.l" "cluster24.orggeom[0]";
connectAttr "cluster24Handle.wm" "cluster24.ma";
connectAttr "cluster24HandleShape.x" "cluster24.x";
connectAttr "defaultRedshiftPostEffects.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of faceSkeleton.ma
