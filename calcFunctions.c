#include <string.h>
#include <math.h>

float simpleCalc(int op1, int op2, char operator) {
	if (operator == '+') {
		float val = (float)(op1 + op2);
 		return val;
	} else if (operator == '-') {
	    float val = (float)(op1 - op2);
		return val;
	} else if (operator == '*') {
	    float val = (float)(op1 * op2);
		return val;
	} else if (operator == '/') {
		float val = (float)op1 / (float)op2;
		return val;
	}
}

//Possible combinations of (o/s/a/h):

//oo, os, oa, oh
//so, ss, sa, sh
//ao, as, aa, ah
//ho, hs, ha, hh

float angCalc(int op1, int op2, char * opType1, char * opType2, char * trig) {
	float ans;

	if (strcmp(trig, "s") == 0) {
		if ((strcmp(opType1, "o") == 0) && (strcmp(opType2, "h") == 0)) {
			float oh = (float)op1 / (float)op2;
			ans = asin(oh)*180/M_PI;
			return ans;
		} else {
			return 383;
		}

	} else if (strcmp(trig, "c") == 0) {
		if ((strcmp(opType1, "s") == 0) && (strcmp(opType2, "h") == 0)) {
			float ah = (float)op1 / (float)op2;
			ans = acos(ah)*180/M_PI;
			return ans;
		} else {
			return 383;
		}

	} else if (strcmp(trig, "t") == 0) {
		if ((strcmp(opType1, "o") == 0) && (strcmp(opType2, "s") == 0)) {
			float os = (float)op1 / (float)op2;
			ans = atan(os)*180/M_PI;
			return ans;
		} else if ((strcmp(opType1, "s") == 0) && (strcmp(opType2, "o") == 0)) {
			float so = (float)op2 / (float)op1;
			ans = atan(so)*180/M_PI;
			return ans;
		} else {
			return 383;
		}

	} else {
		return 383;
	}
}

float sideCalc(int op1, int op2, char * opType1, char * opType2, char * trig) {
	float ans;

	if (strcmp(trig, "s") == 0) {
		if ((strcmp(opType1, "a") == 0) && (strcmp(opType2, "h") == 0)) {
			float opfloat = op1*(M_PI/180);
			ans = op2 * sin(opfloat);
			return ans;
		} else {
			return 383;
		}

	} else if (strcmp(trig, "c") == 0) {
		if ((strcmp(opType1, "a") == 0) && (strcmp(opType2, "h") == 0)) {
			float opfloat = op1*(M_PI/180);
			ans = op2 * cos(opfloat);
			return ans;
		} else {
			return 383;
		}

	} else if (strcmp(trig, "t") == 0) {
		if ((strcmp(opType1, "o") == 0) && (strcmp(opType2, "s") == 0)) {
			float o2 = powf((float)op1, 2);
			float s2 = powf((float)op2, 2);
			ans = sqrt(o2 + s2);
			return ans;
		} else if ((strcmp(opType1, "s") == 0) && (strcmp(opType2, "o") == 0)) {
			float o2 = powf((float)op1, 2);
			float s2 = powf((float)op2, 2);
			ans = sqrt(o2 + s2);
			return ans;
		} else {
			return 383;
		}

	} else {
		return 383;
	}	
}