  //////////////////////////////////////////////
  //                                          //
  //   Code by: Mohammad Ful Hossain Seikh    //
  //   @University of Kansas, USA             //
  //   February 28, 2021                      //
  //   Project1                               //
  //   Computational Physics PHSX 815         //
  //                                          //
  //////////////////////////////////////////////


  // Construction of a Fair Dice
  // The goal is to construct a fair and an unfair dice of six faces using random numbers and find 
  // out the probability of getting odd and even faces using histogram!
  
  
  
  {
  gROOT->Reset();
  #include "TMath.h"
  #include "TRandom.h"
  #include "TStyle.h"
  #include "TCanvas.h"
  
  TH1F *h2 = new TH1F("h2", "Fair Even Distribution", 6, -1, 5);
  TH1F *h3 = new TH1F("h3", "Fair Odd Distribution", 6, -1, 5);
  TH1F *h4 = new TH1F("h4", "Unfair Even Distribution", 6, -1, 5);
  TH1F *h5 = new TH1F("h5", "Unfair Odd Distribution", 6, -1, 5);

	TRandom r;
	r.SetSeed(0);
	ofstream out;
	out.open("OddEven_FairUnfair_Compare.out");
	
	int max = 1000000, entries = 10000;
	int T_all1 = 0, T_all2 = 0, T_all3 = 0, T_all4 = 0, T_all5 = 0, T_all6 = 0;
	int T_Even = 0, T_Odd = 0;
	int unfair_sum_kcount_even = 0, unfair_sum_kcount_odd = 0;
	
	for (int i = 0; i < entries; i++)
	{
	int fair_kcount_even = 0, fair_kcount_odd = 0;
	int unfair_kcount_even = 0, unfair_kcount_odd = 0;
	int T1 = 0, T2 = 0, T3 = 0, T4 = 0, T5 = 0, T6 = 0;
	
	     for (int j = 0; j < 3; j++)
	     {
	     float x = r.Uniform(0, 1);
	     int y = 3*x + 2;
	     
	     int face1 = 0, face2 = 0, face3 = 0;
	     int face4 = 0, face5 = 0, face6 = 0;
	     
	     	if (x < 1./6.)                      {face1++; T1++; fair_kcount_odd++;}
	     	if (x > 1./6. && x < 2./6.)         {face2++; T2++; fair_kcount_even++;}
	     	if (x > 2./6. && x < 3./6.)         {face3++; T3++; fair_kcount_odd++;}
	     	if (x > 3./6. && x < 4./6.)         {face4++; T4++; fair_kcount_even++;}
	     	if (x > 4./6. && x < 5./6.)         {face5++; T5++; fair_kcount_odd++;}
	     	if (x > 5./6.)                      {face6++; T6++; fair_kcount_even++;}
	     	
	     	if (y%2 == 0)
                {
                unfair_kcount_even++;
           	unfair_sum_kcount_even++;
           	}
           
           	if (y%2 == 1)
           	{
           	unfair_kcount_odd++;
           	unfair_sum_kcount_odd++;
           	}
	     
	     }
	     
	     
        T_all1 += T1; T_all2 += T2;
	T_all3 += T3; T_all4 += T4;
	T_all5 += T5; T_all6 += T6;
	
	T_Odd = T1+T3+T5;
	T_Even = T2+T4+T6;
	       
	h2->Fill(T_Odd); 
	h3->Fill(T_Even); 
	
	h4->Fill(unfair_kcount_even);
        h5->Fill(unfair_kcount_odd);
	     
	}
	
	fair_kcount_odd = T_all1 + T_all3 + T_all5;
	fair_kcount_even = T_all3 + T_all4 + T_all6;
	
	
	
	out<< "Total number of rolls: " <<entries*3<<endl;
        out<< "Fair_Even Probability: " <<float(fair_kcount_even)/entries<<endl;
        out<< "Fair_Odd Probability:  " <<float(fair_kcount_odd)/entries<<endl;
        out<< "Unfair_Even Probability: " <<float(unfair_sum_kcount_even)/entries<<endl;
        out<< "Unfair_Odd Probability:  " <<float(unfair_sum_kcount_odd)/entries<<endl;
 	
  
  TCanvas *c1 = new TCanvas("c1", "Fair_Unfair Odd_Even Dice Distribution", 100, 10, 600, 600);
  c1->SetGrid();
  c1->GetFrame()->SetFillColor(10);
  c1->GetFrame()->SetBorderSize(1);
  c1->Divide(2,1);
  
  gStyle->SetOptTitle(kFALSE);
  gStyle->SetOptStat(0);
  
  c1->cd(1);
  gPad->SetGrid();
  h2->SetLineColor(2);
  h4->SetLineColor(3);
  h2->Draw();
  h4->Draw("same");
  gPad->BuildLegend();
  
  c1->cd(2);
  gPad->SetGrid();
  h3->SetLineColor(kBlack);
  h5->SetLineColor(kBlue);
  h3->Draw();
  h5->Draw("same");
  gPad->BuildLegend();
  
  }
