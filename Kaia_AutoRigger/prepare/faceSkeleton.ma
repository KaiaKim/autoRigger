//Maya ASCII 2022 scene
//Name: faceSkeleton.ma
//Last modified: Wed, Jul 27, 2022 10:48:32 PM
//Codeset: 949
requires maya "2022";
requires -nodeType "RedshiftOptions" -nodeType "RedshiftPostEffects" "redshift4maya" "3.0.64";
requires "stereoCamera" "10.0";
requires "mtoa" "4.2.3";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2022";
fileInfo "version" "2022";
fileInfo "cutIdentifier" "202106180615-26a94e7f8c";
fileInfo "osv" "Windows 10 Home v2009 (Build: 19043)";
fileInfo "UUID" "D2657EE4-410F-F940-DD5D-CBA3F9573DA7";
createNode transform -s -n "persp";
	rename -uid "D82E65E5-4C47-4946-6543-25BE34AAF9C2";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 29.366776703148222 150.31166550804915 40.515353500701529 ;
	setAttr ".r" -type "double3" -11.138352729602378 39.000000000000007 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "0365293B-445B-290E-367B-818C1EBDE253";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 47.560130725371209;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 1.430511474609375e-06 141.12405736322285 4.2504062199184371 ;
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
createNode transform -n "lid_upper_r_curve";
	rename -uid "8455998E-4301-EF5C-B7EF-7A9C981FB28A";
createNode nurbsCurve -n "lid_upper_r_curveShape" -p "lid_upper_r_curve";
	rename -uid "064B580A-4E05-4899-E343-C282EAFE097A";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lid_upper_r_curveShapeOrig" -p "lid_upper_r_curve";
	rename -uid "3D73E29F-4A51-8001-D510-DEA1A67C544C";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 3 0 no 3
		6 0 0 0.33333333333333337 0.66666666666666674 1 1
		5
		-2.870902080215247 143.40175017140305 6.8712303854058892
		-2.927262794060709 145.12279187167218 6.8171169149639654
		-4.9873711608169913 145.96410022162803 6.8130764932122876
		-6.9050312399413762 145.01827467771685 5.8165655596147765
		-6.983070167784529 143.83236694335938 5.5843982696533203
		;
createNode transform -n "lid_lower_r_curve";
	rename -uid "7EE464F0-4C12-BC2C-F5D5-D4A49DB17D06";
createNode nurbsCurve -n "lid_lower_r_curveShape" -p "lid_lower_r_curve";
	rename -uid "79E67FB1-4B28-D4AA-B288-E7B4A9D0FADA";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lid_lower_r_curveShapeOrig" -p "lid_lower_r_curve";
	rename -uid "12531719-4503-4D74-AE74-83ABE1CE6F9F";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 3 0 no 3
		6 0 0 0.33333333333333337 0.66666666666666674 1 1
		5
		-2.870902080215247 143.40175017140305 6.8712303854058892
		-3.8660870710125597 143.05619527497618 6.6350729963638742
		-5.1749410629272461 142.94437582128157 6.2767438888549805
		-6.4804145866618965 143.16136243637132 5.8386219817812224
		-6.983070167784529 143.83236694335938 5.5843982696533203
		;
createNode transform -n "lip_upper_curve";
	rename -uid "863E117F-4EBF-1459-F195-6AB563C765A1";
createNode nurbsCurve -n "lip_upper_curveShape" -p "lip_upper_curve";
	rename -uid "849F9059-4FDE-9F2A-8557-149A02EDF3BA";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_upper_curveShapeOrig" -p "lip_upper_curve";
	rename -uid "90BC301A-415F-426F-C2A1-8A8AEE1FA7F7";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 21 ".gtag";
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
		

		"gtag" 21
		"cluster1" 1 "cv[0]"
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
createNode transform -n "lip_lower_curve";
	rename -uid "F1521AF3-4277-A1F2-3FE5-55B7DF944635";
createNode nurbsCurve -n "lip_lower_curveShape" -p "lip_lower_curve";
	rename -uid "E74F9C48-4DB8-AEB7-FF62-2EB7171C6B8E";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lip_lower_curveShapeOrig" -p "lip_lower_curve";
	rename -uid "55DB14B1-4B86-BF5D-8FE6-AD95F000E5C5";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 21 ".gtag";
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
		

		"gtag" 21
		"cluster1" 1 "cv[0]"
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
		"cluster1_9" 1 "cv[5]";
createNode joint -n "face_bind";
	rename -uid "0CE6E9EC-4D78-894F-BF0A-7AA679B679B8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.3019790515124298e-14 139.54475402832031 -2 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3019790515124298e-14 139.54475402832031 -2 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "face_upper_bind" -p "face_bind";
	rename -uid "9637CD37-4C34-F31B-2533-AC98BE5BC7F3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.3019077423250447e-14 1.9910335502158603 0.30000000000000004 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1.0000000000000002 0 7.1309187385013778e-19 141.53578757853617 -1.7 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_upper_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "teeth_upper_bind" -p "face_upper_bind";
	rename -uid "208369D9-4399-1B09-7937-289B04DE0173";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.013299210928380489 -3.4228504500740655 8.7540576876644618 ;
	setAttr ".r" -type "double3" -1.5902773407317584e-15 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 11.32726899590763 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.98052129010354039 0.19641282965653928 0
		 0 -0.19641282965653928 0.98052129010354039 0 0.013299210928380489 138.11293712846211 7.0540576876644634 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "teeth_upper_bind";
	setAttr ".radi" 0.5;
createNode joint -n "eye_socket_l_bind" -p "face_upper_bind";
	rename -uid "5A8162EA-49AA-2FF6-88F9-BD89891C9C76";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.6800000667572021 3.1172122993935147 3.6069999456405633 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.6800000667572021 144.65299987792969 1.9069999456405642 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye_socket";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "eye_l_bind" -p "eye_socket_l_bind";
	rename -uid "062DD998-409B-7B45-739E-57A855230C45";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.3322676295501878e-15 -2.8421709430404007e-14 -4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.6800000667572035 144.65299987792966 1.9069999456405637 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
	setAttr ".radi" 0.5;
createNode joint -n "eye_socket_r_bind" -p "face_upper_bind";
	rename -uid "BF63A6D0-47BD-A66A-5E3A-538F9D4E8AFF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.6800000667572021 3.1172122993935147 3.6069999456405633 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" -1 0 -1.2246467991473532e-16 0 0 1 0 0 1.2246467991473532e-16 0 -1 0
		 -3.6800000667572021 144.65299987792969 1.9069999456405642 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye_socket";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "eye_r_bind" -p "eye_socket_r_bind";
	rename -uid "D09E7DB7-4110-4C5C-68F8-019B74EC340D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.6645352591003757e-15 0 -2.2204460492503131e-16 ;
	setAttr ".r" -type "double3" 0 6.5559993560784401e-16 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 2.4492935982947064e-16 0 0 1 0 0 -2.4492935982947064e-16 0 1 0
		 -3.6800000667571995 144.65299987792969 1.9069999456405644 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
	setAttr ".radi" 0.5;
createNode joint -n "nose_bridge_bind" -p "face_upper_bind";
	rename -uid "26D45A04-4F1E-73AC-274A-0CAB983C4F66";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.019507717542005941 2.3272757301703848 9.5343620802521745 ;
	setAttr ".r" -type "double3" 3.7946955333362383e-19 8.6967464195821412e-17 0.49999999612681673 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -25.21596939126098 0 0 ;
	setAttr ".bps" -type "matrix" 0.99996192306476117 0.0078949694251991553 -0.0037177786916076381 0
		 -0.00872653543077671 0.9046738962540336 -0.42601524505106786 0 -2.1684043449710093e-19 0.42603146702364741 0.90470834477508766 0
		 -0.019507717542005941 143.86306330870656 7.8343620802521761 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nose_brige_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "nose_bind" -p "nose_bridge_bind";
	rename -uid "7B1552CC-4CB8-A0CC-DE4D-99B2711C1913";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -2.2312338326042465 0.20394763669361282 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 23.235886259255395 0 0 ;
	setAttr ".bps" -type "matrix" 1 -6.9388939039072284e-18 4.3368086899420177e-18 0
		 6.8533465540116807e-18 0.99940289822345529 -0.034552091435368637 0 -3.6686991162046965e-18 0.034552091435368693 0.99940289822345529 0
		 -5.2041704279304213e-16 141.93141255994448 8.9694147686645316 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nose_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "sneer_l_bind" -p "nose_bind";
	rename -uid "047EFCC4-465E-7FA2-4BB3-39BCCCD3DB38";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.21903214560501724 2.8421709430404007e-14 3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 9.5416640443905503e-15 -2.0914202703678522e-14 3.3168479978599133e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -15.675133941877899 0 0 ;
	setAttr ".bps" -type "matrix" 1 -6.9388939039072284e-18 4.3368086899420177e-18 0
		 7.5896831226623083e-18 0.95289882536415571 -0.30328835885937405 0 -1.6806017649044133e-18 0.30328835885937411 0.95289882536415571 0
		 0.21903214560501705 141.93141255994448 8.969414768664528 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "sneer";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "nostril_l_bind" -p "sneer_l_bind";
	rename -uid "D1C6B40C-4EBE-689C-1787-A282B0146240";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.27100000000002689 -0.87100000000003774 0.25899999999996481 ;
	setAttr ".r" -type "double3" -2.4947756120139421e-15 1.8726313365963969e-15 3.1805546814635168e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 12.483999999999998 ;
	setAttr ".bps" -type "matrix" 0.97635641039468091 0.20598525391636685 -0.065560926245923301 0
		 -0.21616697222566983 0.93036887660185497 -0.29611753337043228 0 -1.6806017649044133e-18 0.30328835885937411 0.95289882536415571 0
		 0.49003214560504404 141.17998936799685 9.4803797250003345 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nostril";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "sneer_r_bind" -p "nose_bind";
	rename -uid "AA3A4421-4D11-7E44-5D44-1AB45C297DD1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.21903199999999601 -0.00029483793943541059 -3.4056482897781848e-05 ;
	setAttr ".r" -type "double3" -3.6864965361582777e-31 -4.5464826645435698e-15 9.2916088456116959e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 15.674999999999992 180 0 ;
	setAttr ".bps" -type "matrix" -1 2.7074830858901341e-18 -1.2672836472673628e-16 0
		 4.0677231322670454e-17 0.95289953436686914 -0.30328613124144665 0 1.1959080448209269e-16 -0.30328613124144671 -0.95289953436686925 0
		 -0.2190319999999962 141.93111672133057 8.9693909197842583 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "sneer";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "nostril_r_bind" -p "sneer_r_bind";
	rename -uid "AB3A882D-41A5-EB76-C01E-04ABE919642F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.27100000000002111 -0.87100000000006617 -0.25899999999997902 ;
	setAttr ".r" -type "double3" -4.878408510438104e-15 -3.4658203889159066e-15 4.7708320221952767e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 12.483999999999998 ;
	setAttr ".bps" -type "matrix" -0.97635641039468091 0.20598540717933672 -0.065560444708500781 0
		 0.21616697222566986 0.93036956884119926 -0.29611535842138892 0 1.1959080448209269e-16 -0.30328613124144671 -0.95289953436686925 0
		 -0.49003200000001745 141.1796923348885 9.480354119496571 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "nostril";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_r_bind" -p "face_upper_bind";
	rename -uid "2C5BF89E-456A-9880-B84A-B1868447AA26";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -7.4475040435791016 5.0199375191200772 7.5842797279357894 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -17 0 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.8;
	setAttr ".liw" yes;
createNode joint -n "brow_inner_r_bind" -p "brow_r_bind";
	rename -uid "0708F453-4754-6CE5-27AB-028398F12EF4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.5562511657200222 0.87918090820315342 0.87590368682318065 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 17.000000000000004 0 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 0 0
		 0 0 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_inner";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_corrugator_r_bind" -p "brow_inner_r_bind";
	rename -uid "B86A8978-4419-6916-D36F-B586C769F570";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.75251388549804688 0.18975830078125 -0.039598464965820312 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 14.999999999999948 ;
	setAttr ".bps" -type "matrix" -0.96592582628906831 -0.25881904510252052 -1.2246467991473532e-16 0
		 -0.25881904510252052 0.96592582628906842 3.0814879110195774e-33 0 1.1829179713786698e-16 3.1696191514317612e-17 -1 0
		 -3.1426379680633545 147.62466326971466 8.3068027496337891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_corrugator";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_peak_r_bind" -p "brow_r_bind";
	rename -uid "A6F00C58-4E3C-1740-43B5-079ABDD3A980";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.1434083728328748 1.1238403320312784 0.93084834239974512 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -8.0000000000000053 0 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_peak";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_l_bind" -p "face_upper_bind";
	rename -uid "D4180571-49CB-EB13-9088-1AAFAEA0A549";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.4475069046020508 5.0199375191200772 7.5842778205871566 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 197 0 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.8;
	setAttr ".liw" yes;
createNode joint -n "brow_inner_l_bind" -p "brow_l_bind";
	rename -uid "C583916F-45C3-A458-D1D9-28BD0E6B5EA2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.5562500257159169 0.879180908203125 -0.87590403535741324 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -17.000000000000011 0 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 0 0
		 0 0 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_inner";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_corrugator_l_bind" -p "brow_inner_l_bind";
	rename -uid "134A0486-4E11-D6A0-BBDE-DBA9938F20A0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.75251186431884776 0.190093994140625 0.039599307250975713 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 14.999999999999993 ;
	setAttr ".bps" -type "matrix" -0.96592582628906831 -0.25881904510252052 -1.2246467991473532e-16 0
		 -0.25881904510252052 0.96592582628906842 3.0814879110195774e-33 0 1.1829179713786698e-16 3.1696191514317612e-17 -1 0
		 -3.1426379680633545 147.62466326971466 8.3068027496337891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_corrugator";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "brow_peak_l_bind" -p "brow_l_bind";
	rename -uid "73BFFEC6-48F2-79ED-5B4C-32836FBE7F47";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.143409031563444 1.1242749023437568 -0.93085391595703548 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 7.999999999999984 0 ;
	setAttr ".bps" -type "matrix" 1 -2.4492935982947064e-16 0 0 2.4492935982947064e-16 1 2.4492935982947064e-16 0
		 -5.9990391306474304e-32 -2.4492935982947064e-16 1 0 7.1309187385001452e-19 146.16157218770294 -2.0409458766457265 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow_peak";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "face_lower_bind" -p "face_bind";
	rename -uid "4E865F98-44B6-8181-6CD1-AFA727A21AFD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.3019790515124298e-14 3.3767878331888141 0.30000000000000004 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 142.92154186150913 -1.7 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "face_lower_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "jaw_trans_bind" -p "face_lower_bind";
	rename -uid "1565CEE9-446D-A5A6-8973-ECB2FC8C348A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -1.6262223533614701 0.80781305096721234 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 141.29531950814766 -0.89218694903278761 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "jaw_trans_bind";
	setAttr ".radi" 0.5;
createNode joint -n "jaw_bind" -p "jaw_trans_bind";
	rename -uid "4213A158-4C51-4FBC-6638-318344991297";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 2.8421709430404007e-14 7.5495165674510645e-15 ;
	setAttr ".r" -type "double3" -9.5416640443905503e-15 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "zyx";
	setAttr ".jo" -type "double3" 16 -5.1795300564603845e-08 -7.6118917757488288e-09 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96126169593831889 0.27563735581699911 0
		 0 -0.27563735581699911 0.96126169593831889 0 0 141.29531950814768 -0.89218694903278006 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "jaw_bind";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "jaw_tip_bind" -p "jaw_bind";
	rename -uid "C250BD0F-4DD0-A5CF-2453-C2BC8D4233D2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 1.8873791418627661e-15 10.201820369305253 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.98052129010354039 0.19641282965653953 0
		 0 -0.19641282965653953 0.98052129010354039 0 0 146.72480613686366 6.7018096387646464 1;
	setAttr ".radi" 0.5;
createNode joint -n "teeth_lower_bind" -p "jaw_bind";
	rename -uid "E052629F-4B06-926C-5A02-F3A251615FA1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.013299211103944053 -0.82754497239673697 8.6741377752063009 ;
	setAttr ".r" -type "double3" -8.7465253740246703e-15 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.6727310040923582 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.9805212901035405 0.19641282965653939 0
		 0 -0.19641282965653939 0.9805212901035405 0 0.013299211103944053 138.10891582416616 7.2178271315535767 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "teeth_lower_bind";
	setAttr ".radi" 0.5;
createNode joint -n "tongue_01_bind" -p "jaw_bind";
	rename -uid "03E7967E-4B67-D631-DE9C-4CBD7E7C0620";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0030725002288818359 -3.4246841840181048 1.8380257388361159 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -89.836765808021809 -44.853409073322815 89.768559727384016 ;
	setAttr ".radi" 0.5;
createNode joint -n "tongue_02_bind" -p "tongue_01_bind";
	rename -uid "F7720D50-4B01-C064-7947-E984C71D39B5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.0922135892475495 0 -4.163336342344337e-16 ;
	setAttr ".r" -type "double3" -9.6115492790906783e-15 -1.8213984887959323e-14 1.0353893355160852e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.014850833216278076 -0.17534171849976721 -5.1932256986906999 ;
	setAttr ".radi" 0.5;
createNode joint -n "tongue_03_bind" -p "tongue_02_bind";
	rename -uid "9F7C7AEF-455A-1982-E21E-33BD2F9974DA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.97012304404439931 0 -5.8980598183211441e-17 ;
	setAttr ".r" -type "double3" -3.8506400334172095e-15 6.6173491570675377e-15 -2.4649298082281377e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -0.0013927326158608864 0.002372099859528921 -4.324615664562268 ;
	setAttr ".radi" 0.51213660487867185;
createNode joint -n "tongue_04_bind" -p "tongue_03_bind";
	rename -uid "CEBE9B7C-42A3-6AB8-D6EF-68BC73B8133C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.90979273979385056 2.8421709430404007e-14 4.3628295420816698e-16 ;
	setAttr ".r" -type "double3" -2.3259820161840893e-14 -2.110053626955245e-14 -1.5900861090733693e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -0.0012832083854923168 -0.0021062089177069244 -12.125974446334952 ;
	setAttr ".radi" 0.5;
createNode joint -n "tongue_05_bind" -p "tongue_04_bind";
	rename -uid "B7A5B4F6-4C67-AB7E-7D82-95B29615D0DA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.1283062947854638 -2.8421709430404007e-14 -9.0639301619788171e-16 ;
	setAttr ".r" -type "double3" 3.9605903761080916e-14 -6.8866075027415927e-15 4.48704667009025e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -0.0038902747468428237 0.013658774369633028 -17.873739456164731 ;
	setAttr ".radi" 0.5;
createNode joint -n "tongue_06_bind" -p "tongue_05_bind";
	rename -uid "1AAAE5AE-4E2D-9B31-4676-4A93A7026C26";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.0255066637163743 5.6843418860808015e-14 1.3473922498563606e-15 ;
	setAttr ".r" -type "double3" 1.5777562361813188e-14 1.9253438274331002e-14 -3.9496972919298961e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.00022470953137651236 0.019155127003792575 -2.1349678959290395 ;
	setAttr ".radi" 0.50398460503276088;
createNode joint -n "tongue_07_bind" -p "tongue_06_bind";
	rename -uid "AD8032AC-4F19-B213-F7E9-D49542BC521E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.0753883307187557 -2.8421709430404007e-14 -1.7433970933566911e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 6.1224124612957134e-14 2.4425666030301852e-14 0 ;
	setAttr ".radi" 0.50398460503276088;
createNode joint -n "cheek_upper_r_bind" -p "face_bind";
	rename -uid "AC49C1DB-4AAC-C5FD-2A16-6AB639D624A5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.0194792747497843 1.6615600585937216 9.2503585815429652 ;
	setAttr ".r" -type "double3" 4.4001128408687519e-31 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 170 25.000000000000007 171 ;
	setAttr ".bps" -type "matrix" -0.89514963424668026 0.14177777382687393 -0.42261826174069961 0
		 0.081574497416672664 0.98416337441241075 0.1573786956242626 0 0.43823821567641952 0.10640260952567288 -0.89253893528902983 0
		 -5.0194792747497514 141.20631408691409 7.2503585815429732 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_r_bind" -p "face_bind";
	rename -uid "A4A3F95E-49A7-2894-D688-46B397FB34DE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -6.3155222335360337 -0.33379007556305851 8.1109353515469067 ;
	setAttr ".r" -type "double3" 3.8166656177562195e-14 0 2.4848083448933718e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 155.00000000000006 39.999999999999915 169 ;
	setAttr ".bps" -type "matrix" -0.75197004909461707 0.14616817060531706 -0.64278760968653925 0
		 -0.093731058820309424 0.94149034561144784 0.32374437096706443 0 0.65249945124656117 0.30369523378270435 -0.69427204401488463 0
		 -6.3155222335360017 139.21096395275728 6.1109353515469138 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_lower_r_bind" -p "face_bind";
	rename -uid "EC1FBE8E-47A9-6426-0696-B09F19BBF500";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.3362746238708834 -2.8736419677733238 7.2705068588257085 ;
	setAttr ".r" -type "double3" 4.7708320221952748e-14 0 1.2722218725854061e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 137.98803651662627 39.952313064542324 162.31499302013259 ;
	setAttr ".bps" -type "matrix" -0.7303514067889878 0.2328743016850463 -0.64214981290665241 0
		 -0.18375779411905063 0.83845213017616316 0.51306052128725987 0 0.65789048914074377 0.49271450660372917 -0.56957222481472602 0
		 -5.3362746238708505 136.67111206054699 5.2705068588257085 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_upper_l_bind" -p "face_bind";
	rename -uid "4BD53B8A-4FCA-5A14-A03A-DCAAF7B08CC4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.019483089446986 1.66156005859375 9.2503566741943359 ;
	setAttr ".r" -type "double3" 0 0 7.1562480332929135e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 10.000000000000012 25.000000000000004 9.0000000000000071 ;
	setAttr ".bps" -type "matrix" 0.89514963424668026 0.14177777382687393 -0.42261826174069944 0
		 -0.081574497416672637 0.98416337441241075 0.15737869562426277 0 0.43823821567641935 -0.10640260952567306 0.89253893528903006 0
		 5.0194830894470224 141.20631408691403 7.2503566741943315 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "brow";
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_l_bind" -p "face_bind";
	rename -uid "32FA2743-4189-0961-0CDC-65861D4AEB0E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.315999999999967 -0.33375402832029977 8.111 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 24.999999999999989 39.99999999999995 10.999999999999989 ;
	setAttr ".bps" -type "matrix" 0.75197004909461695 0.14616817060531687 -0.64278760968653892 0
		 0.093731058820309771 0.94149034561144773 0.3237443709670646 0 0.65249945124656084 -0.30369523378270474 0.69427204401488418 0
		 5.8340487480163423 138.73069763183588 6.3339762687682724 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cheek_lower_l_bind" -p "face_bind";
	rename -uid "4C8EF6EA-4D42-F0AE-D2C6-89BCD37CA1AE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.3359999999999674 -2.8737540283203202 7.271 ;
	setAttr ".r" -type "double3" 7.951386703658789e-16 5.8641476939483593e-15 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 42.011963483373762 39.952313064542338 17.685006979867453 ;
	setAttr ".bps" -type "matrix" 0.7303514067889878 0.2328743016850465 -0.6421498129066523 0
		 0.18375779411905019 0.83845213017616349 0.51306052128725965 0 0.65789048914074399 -0.49271450660372867 0.56957222481472602 0
		 5.2382864952087518 136.72753906250006 5.2657613754272754 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "CADFADD4-4172-F931-4D78-E7BB0C3D4988";
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
	rename -uid "F4F62299-4AF7-4840-1375-A6950251A0A7";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "9FD4B593-43AB-B714-E209-83960B675F17";
createNode displayLayerManager -n "layerManager";
	rename -uid "92D9B8F8-4991-E6B7-C6C3-C28D18F0F769";
createNode displayLayer -n "defaultLayer";
	rename -uid "CD90B0CD-41FB-C9C5-89C6-DF92BC3B2AFB";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "3CB5E2FB-4376-6763-86A1-1AAC9F3B3B60";
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
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1170\n            -height 734\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|front|frontShape\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n"
		+ "            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n"
		+ "            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n"
		+ "            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|persp|perspShape\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n"
		+ "            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n"
		+ "            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n"
		+ "            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1170\n            -height 734\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1170\\n    -height 734\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1170\\n    -height 734\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 50 -size 100 -divisions 3 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "2895A3EC-41BB-018A-A872-758E37F9EEE6";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
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
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
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
connectAttr "lid_upper_r_curveShapeOrig.ws" "lid_upper_r_curveShape.cr";
connectAttr "lid_lower_r_curveShapeOrig.ws" "lid_lower_r_curveShape.cr";
connectAttr "lip_upper_curveShapeOrig.ws" "lip_upper_curveShape.cr";
connectAttr "lip_lower_curveShapeOrig.ws" "lip_lower_curveShape.cr";
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
connectAttr "brow_r_bind.s" "brow_inner_r_bind.is";
connectAttr "brow_inner_r_bind.s" "brow_corrugator_r_bind.is";
connectAttr "brow_r_bind.s" "brow_peak_r_bind.is";
connectAttr "face_upper_bind.s" "brow_l_bind.is";
connectAttr "brow_l_bind.s" "brow_inner_l_bind.is";
connectAttr "brow_inner_l_bind.s" "brow_corrugator_l_bind.is";
connectAttr "brow_l_bind.s" "brow_peak_l_bind.is";
connectAttr "face_bind.s" "face_lower_bind.is";
connectAttr "face_lower_bind.s" "jaw_trans_bind.is";
connectAttr "jaw_trans_bind.s" "jaw_bind.is";
connectAttr "jaw_bind.s" "jaw_tip_bind.is";
connectAttr "jaw_bind.s" "teeth_lower_bind.is";
connectAttr "jaw_bind.s" "tongue_01_bind.is";
connectAttr "tongue_01_bind.s" "tongue_02_bind.is";
connectAttr "tongue_02_bind.s" "tongue_03_bind.is";
connectAttr "tongue_03_bind.s" "tongue_04_bind.is";
connectAttr "tongue_04_bind.s" "tongue_05_bind.is";
connectAttr "tongue_05_bind.s" "tongue_06_bind.is";
connectAttr "tongue_06_bind.s" "tongue_07_bind.is";
connectAttr "face_bind.s" "cheek_upper_r_bind.is";
connectAttr "face_bind.s" "cheek_r_bind.is";
connectAttr "face_bind.s" "cheek_lower_r_bind.is";
connectAttr "face_bind.s" "cheek_upper_l_bind.is";
connectAttr "face_bind.s" "cheek_l_bind.is";
connectAttr "face_bind.s" "cheek_lower_l_bind.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "defaultRedshiftPostEffects.msg" ":redshiftOptions.postEffects";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "defaultRedshiftPostEffects.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of faceSkeleton.ma
