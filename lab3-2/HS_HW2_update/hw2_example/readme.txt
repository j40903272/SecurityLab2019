//====================== Example ========================
//
// 'Ciphertext.csv' and 'Trace.csv' in the sub-directories are the example input files.
//
// The ciphertexts are derived with the following key:
//
//   key: 3220db6534d687f844c41b6de5a4c737 (student_ID = r06921000)
//        (with byte0 = 32 and byte15 = 37)
//
// Traces in case1 are generated with the same scheme as specified in HW1,
// while those in case2 with a slightly different scheme.
// An effective CPA program should recover the key, though.
//
// Samples per trace: 2560 in case1 / 3200 in case2
//
// FYI, 'Plaintext.csv' are also provided.
//
// Since the leakage point numbers and correlation coefficients depend on which
// intermediate value you've chosen, the result files are not offered.
// Please refer to the PDF for the formats of the result files.
//

//================== Grading Policy =====================
//
// HW1: Correctness: 25 %
//      Report     :  5 %
//
// HW2: Correctness: 45 %
//      Report     : 10 %
//      Performance: 15 %
//
// General Rules for performance Evaluation (3200 samples per trace):
//
//    | Time to convergence | Points |
//    |               < 10s |   > 12 |
//    |           10s - 12s |     12 |
//    |           12s - 15s |     10 |
//    |           15s - 20s |      8 |
//    |           20s - 30s |      7 |
//    |           30s - 60s |      6 |
//    |               > 60s |    < 5 | (TLE)
//
//    We reserve the right to make adjustments.
//
//    Since we don't yet specify the platform, the table just give rough
//    intervals for reference. By the way, you may receive 9 or 11 points or so.
//    
//    FYI, the reference program solves the case1 in around 10s and case2 12s.
//    (Platform: Intel i5U / AMD A10)
//    
//    Note that if your program can not solve the problem correctly,
//    you will get less than 5 points for this part.
//
