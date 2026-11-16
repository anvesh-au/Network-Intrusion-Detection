# H6 report (mean of 2 seeds)

## Summary

| config | benign_fpr | web detect/named | infiltration detect/named | portscan detect/named | bot detect/named | ddos detect/named | probe bruteforce named first->last | probe dos named first->last | probe heartbleed named first->last | labels/block | contam (attacks in benign adds, total/seed) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A0 | 0.012 | 0.87/0.00 | 0.97/0.00 | 0.91/0.00 | 0.06/0.00 | 1.00/0.00 | 0.99->0.99 | 0.89->0.89 | 0.75->0.75 | 0.0 | 0.0 |
| A1_B1_B100 | 0.012 | 0.87/0.15 | 0.97/0.00 | 0.90/0.45 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.89 | 0.75->0.75 | 78.75 | 98.0 |
| A1_B1_B500 | 0.012 | 0.87/0.17 | 0.97/0.00 | 0.95/0.82 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.90 | 0.75->0.75 | 241.45 | 77.5 |
| A1_B2_B100 | 0.012 | 0.87/0.08 | 0.97/0.00 | 0.94/0.77 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.89 | 0.75->0.75 | 78.075 | 84.5 |
| A1_B2_B500 | 0.011 | 0.87/0.17 | 0.97/0.00 | 0.94/0.81 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.90 | 0.75->0.75 | 237.875 | 74.0 |
| A2_B1_B100 | 0.012 | 0.87/0.15 | 0.97/0.00 | 0.94/0.41 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.00 | 0.75->0.75 | 78.875 | 78.0 |
| A2_B1_B500 | 0.012 | 0.87/0.17 | 0.97/0.00 | 0.94/0.81 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.09 | 0.75->0.75 | 240.4 | 83.5 |
| A2_B2_B100 | 0.012 | 0.87/0.08 | 0.97/0.00 | 0.90/0.37 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.00 | 0.75->0.75 | 78.025 | 109.0 |
| A2_B2_B500 | 0.011 | 0.87/0.17 | 0.97/0.00 | 0.90/0.78 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.00 | 0.75->0.75 | 236.55 | 119.5 |
| A3_B1_B100_r0.5 | 0.012 | 0.87/0.00 | 0.97/0.00 | 0.90/0.14 | 0.06/0.00 | 1.00/0.61 | 0.99->0.99 | 0.88->0.88 | 0.00->0.00 | 78.85 | 107.5 |
| A3_B1_B100_r1.0 | 0.012 | 0.87/0.00 | 0.97/0.00 | 0.84/0.03 | 0.06/0.00 | 1.00/0.30 | 0.99->0.99 | 0.89->0.89 | 0.00->0.00 | 78.675 | 142.0 |
| A3_B1_B100_r2.0 | 0.012 | 0.87/0.00 | 0.97/0.00 | 0.85/0.03 | 0.06/0.00 | 1.00/0.00 | 0.99->0.99 | 0.89->0.89 | 0.25->0.25 | 78.7 | 136.0 |
| A3_B1_B500_r0.5 | 0.012 | 0.87/0.13 | 0.97/0.00 | 0.87/0.13 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.88->0.88 | 0.00->0.00 | 241.375 | 140.5 |
| A3_B1_B500_r1.0 | 0.012 | 0.87/0.00 | 0.97/0.00 | 0.83/0.04 | 0.06/0.00 | 1.00/0.29 | 0.99->0.99 | 0.89->0.89 | 0.00->0.00 | 239.1 | 163.0 |
| A3_B1_B500_r2.0 | 0.012 | 0.87/0.00 | 0.97/0.00 | 0.84/0.04 | 0.06/0.00 | 1.00/0.00 | 0.99->0.99 | 0.89->0.89 | 0.25->0.25 | 240.3 | 161.5 |
| A3b_B1_B100_r0.5 | 0.012 | 0.87/0.12 | 0.97/0.00 | 0.93/0.18 | 0.06/0.00 | 1.00/0.82 | 0.99->0.99 | 0.89->0.89 | 0.00->0.00 | 79.15 | 87.0 |
| A3b_B1_B100_r1.0 | 0.012 | 0.87/0.17 | 0.97/0.00 | 0.91/0.33 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.89 | 0.00->0.00 | 78.75 | 94.0 |
| A3b_B1_B100_r2.0 | 0.012 | 0.87/0.17 | 0.97/0.00 | 0.90/0.75 | 0.06/0.00 | 1.00/0.68 | 0.99->0.99 | 0.89->0.89 | 0.25->0.25 | 78.825 | 108.5 |
| A3b_B1_B500_r0.5 | 0.012 | 0.87/0.14 | 0.97/0.00 | 0.90/0.17 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.89 | 0.00->0.00 | 240.5 | 107.0 |
| A3b_B1_B500_r1.0 | 0.012 | 0.87/0.17 | 0.97/0.03 | 0.87/0.31 | 0.06/0.00 | 1.00/0.83 | 0.99->0.99 | 0.89->0.89 | 0.00->0.00 | 240.6 | 131.0 |
| A3b_B1_B500_r2.0 | 0.012 | 0.87/0.17 | 0.97/0.24 | 0.91/0.76 | 0.06/0.00 | 1.00/0.66 | 0.99->0.99 | 0.89->0.89 | 0.25->0.25 | 240.725 | 96.0 |

## A0

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500426 | 494374 | 24 | 78 | 4 | 0 | 0 | 0 | 0 | 0 | 5946 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 90 |
| infiltration | 37 | 1 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 22 |
| portscan | 7698 | 659 | 30 | 76 | 0 | 0 | 0 | 0 | 0 | 0 | 6933 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 39785 | 0 | 0 | 0 | 0 | 0 | 0 | 55359 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A1_B1_B100

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500424 | 494380 | 26 | 76 | 6 | 2 | 0 | 198 | 0 | 0 | 5736 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 74 |
| infiltration | 36 | 1 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 21 |
| portscan | 7698 | 765 | 30 | 32 | 0 | 0 | 0 | 3441 | 0 | 0 | 3430 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 5982 | 0 | 0 | 0 | 84 | 0 | 79251 | 9827 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3001 | 166 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A1_B1_B500

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494595 | 26 | 81 | 3 | 11 | 0 | 314 | 0 | 0 | 5395 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 72 |
| infiltration | 36 | 1 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 22 |
| portscan | 7699 | 398 | 30 | 22 | 0 | 0 | 0 | 6305 | 0 | 0 | 944 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 5107 | 0 | 0 | 0 | 3219 | 0 | 79144 | 7674 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 159 | 0 | 2685 | 0 | 0 | 0 | 0 | 0 | 0 | 156 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A1_B2_B100

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494552 | 24 | 83 | 3 | 4 | 0 | 218 | 0 | 0 | 5541 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 82 |
| infiltration | 36 | 1 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 22 |
| portscan | 7697 | 482 | 31 | 44 | 0 | 0 | 0 | 5922 | 0 | 0 | 1218 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 6356 | 0 | 0 | 0 | 0 | 0 | 79243 | 9545 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 164 | 0 | 2684 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A1_B2_B500

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500424 | 494798 | 24 | 76 | 2 | 14 | 0 | 18 | 0 | 0 | 5492 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 72 |
| infiltration | 36 | 1 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 21 |
| portscan | 7697 | 490 | 29 | 21 | 0 | 0 | 0 | 6240 | 0 | 0 | 917 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95145 | 0 | 0 | 5086 | 0 | 0 | 0 | 3264 | 0 | 79095 | 7700 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3001 | 166 | 0 | 2685 | 0 | 0 | 0 | 0 | 0 | 0 | 150 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A2_B1_B100

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500426 | 494420 | 18 | 24 | 4 | 11 | 0 | 66 | 0 | 0 | 5883 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 74 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7698 | 428 | 20 | 0 | 0 | 0 | 0 | 3144 | 0 | 0 | 4106 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 43 | 0 | 79277 | 15824 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 26 | 2745 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| dos | 3001 | 2434 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 566 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A2_B1_B500

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500426 | 494588 | 18 | 31 | 3 | 12 | 0 | 340 | 0 | 0 | 5434 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 72 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7697 | 452 | 24 | 0 | 0 | 0 | 0 | 6214 | 0 | 0 | 1007 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 2368 | 0 | 79132 | 13644 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 29 | 2741 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 2998 | 2214 | 0 | 256 | 0 | 0 | 0 | 42 | 0 | 10 | 476 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A2_B2_B100

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494608 | 18 | 27 | 7 | 2 | 0 | 32 | 0 | 0 | 5731 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 82 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7698 | 770 | 24 | 0 | 0 | 0 | 0 | 2842 | 0 | 0 | 4062 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 79277 | 15867 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 30 | 2741 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| dos | 3000 | 2452 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 547 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A2_B2_B500

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500424 | 494993 | 18 | 27 | 2 | 9 | 0 | 313 | 0 | 0 | 5062 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 72 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7698 | 766 | 20 | 0 | 0 | 0 | 0 | 5978 | 0 | 0 | 934 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 3280 | 0 | 79144 | 12720 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 165 | 0 | 2683 | 0 | 0 | 0 | 0 | 0 | 0 | 152 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 27 | 2744 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| dos | 3000 | 2473 | 0 | 1 | 0 | 0 | 0 | 76 | 0 | 10 | 440 |
| heartbleed | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3_B1_B100_r0.5

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494439 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5985 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 90 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7698 | 740 | 0 | 0 | 0 | 0 | 0 | 1064 | 0 | 0 | 5894 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 72 | 0 | 58054 | 37018 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2741 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| dos | 3001 | 167 | 0 | 2650 | 0 | 0 | 0 | 0 | 0 | 0 | 184 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2741 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| dos | 3001 | 165 | 0 | 2650 | 0 | 0 | 0 | 0 | 0 | 0 | 186 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3_B1_B100_r1.0

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494439 | 3 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 5976 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 90 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7698 | 1196 | 10 | 12 | 0 | 0 | 0 | 230 | 0 | 0 | 6250 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 91 | 0 | 28408 | 66645 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2748 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 167 | 0 | 2660 | 0 | 0 | 0 | 0 | 0 | 0 | 173 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2748 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 160 | 0 | 2658 | 0 | 0 | 0 | 0 | 0 | 0 | 182 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3_B1_B100_r2.0

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500424 | 494432 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 5976 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 90 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7698 | 1142 | 10 | 40 | 0 | 0 | 0 | 196 | 0 | 0 | 6310 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95143 | 0 | 0 | 3030 | 0 | 0 | 0 | 0 | 0 | 12 | 92101 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2750 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 2999 | 167 | 0 | 2660 | 0 | 0 | 0 | 0 | 0 | 0 | 172 |
| heartbleed | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2750 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 3000 | 160 | 0 | 2660 | 0 | 0 | 0 | 0 | 0 | 0 | 180 |
| heartbleed | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3_B1_B500_r0.5

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494550 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5874 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 76 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7698 | 974 | 0 | 0 | 0 | 0 | 0 | 1026 | 0 | 0 | 5698 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 34 | 0 | 78678 | 16432 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2741 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| dos | 3001 | 167 | 0 | 2650 | 0 | 0 | 0 | 0 | 0 | 0 | 184 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2741 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| dos | 3000 | 164 | 0 | 2651 | 0 | 0 | 0 | 0 | 0 | 0 | 185 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3_B1_B500_r1.0

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500424 | 494566 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 5852 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 90 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7698 | 1336 | 10 | 25 | 0 | 0 | 0 | 323 | 0 | 0 | 6004 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95145 | 0 | 0 | 0 | 0 | 0 | 0 | 1759 | 0 | 28064 | 65322 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2748 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 167 | 0 | 2660 | 0 | 0 | 0 | 0 | 0 | 0 | 173 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2748 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 163 | 0 | 2659 | 0 | 0 | 0 | 0 | 0 | 0 | 178 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3_B1_B500_r2.0

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500426 | 494557 | 8 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 5855 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 90 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| portscan | 7699 | 1264 | 10 | 38 | 0 | 0 | 0 | 330 | 0 | 0 | 6057 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 3468 | 0 | 0 | 0 | 92 | 0 | 0 | 91584 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2750 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 2999 | 167 | 0 | 2660 | 0 | 0 | 0 | 0 | 0 | 0 | 172 |
| heartbleed | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 22 | 2750 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dos | 2999 | 158 | 0 | 2658 | 0 | 0 | 0 | 0 | 0 | 0 | 183 |
| heartbleed | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3b_B1_B100_r0.5

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494447 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5976 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 78 |
| infiltration | 36 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 32 |
| portscan | 7699 | 534 | 0 | 0 | 0 | 0 | 0 | 1423 | 0 | 0 | 5742 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 111 | 0 | 77618 | 17415 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 26 | 2744 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 174 | 0 | 2660 | 0 | 0 | 0 | 0 | 0 | 0 | 166 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 26 | 2744 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 164 | 0 | 2660 | 0 | 0 | 0 | 0 | 0 | 0 | 176 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3b_B1_B100_r1.0

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494399 | 4 | 8 | 0 | 0 | 0 | 2 | 0 | 0 | 6012 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 72 |
| infiltration | 36 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 33 |
| portscan | 7698 | 657 | 12 | 10 | 0 | 0 | 0 | 2514 | 0 | 0 | 4505 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 3266 | 0 | 78992 | 12886 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2752 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 166 | 0 | 2672 | 0 | 0 | 0 | 0 | 0 | 0 | 162 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2752 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 172 | 0 | 2672 | 0 | 0 | 0 | 0 | 0 | 0 | 156 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3b_B1_B100_r2.0

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494408 | 11 | 18 | 0 | 0 | 0 | 344 | 0 | 0 | 5644 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 72 |
| infiltration | 36 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 32 |
| portscan | 7698 | 795 | 22 | 13 | 0 | 0 | 0 | 5762 | 0 | 0 | 1106 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95146 | 0 | 0 | 1512 | 0 | 0 | 0 | 12932 | 0 | 64236 | 16466 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2752 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 166 | 0 | 2674 | 0 | 0 | 0 | 0 | 0 | 0 | 160 |
| heartbleed | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2752 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 156 | 0 | 2677 | 0 | 0 | 0 | 0 | 0 | 0 | 167 |
| heartbleed | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3b_B1_B500_r0.5

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500425 | 494584 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5839 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 76 |
| infiltration | 36 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 32 |
| portscan | 7698 | 758 | 0 | 0 | 0 | 0 | 0 | 1312 | 0 | 0 | 5628 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 10 | 0 | 0 | 0 | 0 | 0 | 88 | 0 | 78718 | 16328 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 26 | 2744 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 174 | 0 | 2660 | 0 | 0 | 0 | 0 | 0 | 0 | 166 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 26 | 2744 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 2999 | 177 | 0 | 2660 | 0 | 0 | 0 | 0 | 0 | 0 | 162 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3b_B1_B500_r1.0

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500426 | 494511 | 5 | 6 | 0 | 0 | 3 | 3 | 0 | 0 | 5898 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 72 |
| infiltration | 36 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 34 |
| portscan | 7699 | 1017 | 12 | 10 | 0 | 0 | 0 | 2376 | 0 | 0 | 4284 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95144 | 0 | 0 | 0 | 0 | 0 | 0 | 3292 | 0 | 78996 | 12856 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2752 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 166 | 0 | 2672 | 0 | 0 | 0 | 0 | 0 | 0 | 162 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2752 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 162 | 0 | 2672 | 0 | 0 | 0 | 0 | 0 | 0 | 166 |
| heartbleed | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## A3b_B1_B500_r2.0

**Replay (Thu+Fri), true class x predicted, flows:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 500424 | 494594 | 10 | 18 | 0 | 0 | 8 | 26 | 0 | 0 | 5768 |
| bruteforce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| heartbleed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| web | 104 | 14 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 72 |
| infiltration | 36 | 1 | 0 | 1 | 0 | 0 | 8 | 0 | 0 | 0 | 26 |
| portscan | 7698 | 688 | 22 | 13 | 0 | 0 | 0 | 5844 | 0 | 0 | 1131 |
| bot | 736 | 692 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 44 |
| ddos | 95143 | 0 | 0 | 2842 | 0 | 0 | 0 | 19792 | 0 | 62603 | 9906 |

**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2752 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| dos | 3000 | 166 | 0 | 2674 | 0 | 0 | 0 | 0 | 0 | 0 | 160 |
| heartbleed | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Known-attack probe, last block:**

| true \ pred | n | benign | bruteforce | dos | heartbleed | web | infiltration | portscan | bot | ddos | unknown |
|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bruteforce | 2773 | 18 | 2753 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| dos | 3000 | 158 | 0 | 2674 | 0 | 0 | 0 | 0 | 0 | 0 | 168 |
| heartbleed | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| web | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| infiltration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| portscan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ddos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
