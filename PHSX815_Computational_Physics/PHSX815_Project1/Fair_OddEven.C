//////////////////////////////////////////////
  //                                          //
  //   Code by: Mohammad Ful Hossain Seikh    //
  //   @University of Kansas, USA             //
  //   February 21, 2021                      //
  //   Project1                               //
  //   Computational Physics PHSX 815         //
  //                                          //
  //////////////////////////////////////////////


  // Construction of a Fair Dice
  // The goal is to construct a fair dice of six faces using random numbers and find 
  // out the probability of getting odd and even faces using histogram!

  {
  gROOT->Reset();
  #include "TMath.h"
  #include "TRandom.h"
  #include "TStyle.h"
  #include "TCanvas.h"
  
  TH1F *h1 = new TH1F("h1", "Fair Uniform Distribution", 100, -2, 3);
  TH1F *h2 = new TH1F("h2", "Fair Even Distribution", 6, -1, 5);
  TH1F *h3 = new TH1F("h3", "Fair Odd Distribution", 6, -1, 5);
  h1->SetXTitle("Interval");
  h1->SetYTitle("Frequency");

	TRandom r;
	r.SetSeed(0);
	ofstream out;
	out.open("Fair_OddEven.out");
	
	int max = 1000000, entries = 10000;
	int T_all1 = 0, T_all2 = 0, T_all3 = 0, T_all4 = 0, T_all5 = 0, T_all6 = 0;
	int T_Even = 0, T_Odd = 0;
	
	out<<"attempt"<<"  "<<"Even"<<"  "<<"Odd"<<"  "<<"Total_Even"<<"  "<<"Total_Odd"<<endl;
	for (int i = 0; i < entries; i++)
	{
	int kcount_even = 0, kcount_odd = 0;
	int T1 = 0, T2 = 0, T3 = 0, T4 = 0, T5 = 0, T6 = 0;
	
	     for (int j = 0; j < 3; j++)
	     {
	     float x = r.Uniform(0, 1);
	     h1->Fill(x);
	     
	     int face1 = 0, face2 = 0, face3 = 0;
	     int face4 = 0, face5 = 0, face6 = 0;
	     
	     	if (x < 1./6.)                      {face1++; T1++; kcount_odd++;}
	     	if (x > 1./6. && x < 2./6.)         {face2++; T2++; kcount_even++;}
	     	if (x > 2./6. && x < 3./6.)         {face3++; T3++; kcount_odd++;}
	     	if (x > 3./6. && x < 4./6.)         {face4++; T4++; kcount_even++;}
	     	if (x > 4./6. && x < 5./6.)         {face5++; T5++; kcount_odd++;}
	     	if (x > 5./6.)                      {face6++; T6++; kcount_even++;}
	     
	     }
	     
	     
        T_all1 += T1; T_all2 += T2;
	T_all3 += T3; T_all4 += T4;
	T_all5 += T5; T_all6 += T6;
	
	T_Odd = T1+T3+T5;
	T_Even = T2+T4+T6;
	       
	h2->Fill(T_Odd); 
	h3->Fill(T_Even); 
	
	out<<i<<"\t"<<kcount_even<<"\t"<<kcount_odd<<" \t"<<T_Even<<"\t"<<T_Odd<<endl;      
	}
	kcount_odd = T_all1 + T_all3 + T_all5;
	kcount_even = T_all3 + T_all4 + T_all6;
	
	
	
	out<< "Total number of rolls: " <<entries*3<<endl;
        out<< "Even Probability: " <<float(kcount_even)/entries<<endl;
        out<< "Odd Probability:  " <<float(kcount_odd)/entries<<endl;
 	
  
  TCanvas *c2 = new TCanvas("c2", "Fair Dice Odd Even", 100, 10, 600, 600);
  c2->cd();
  c2->SetGrid();
  h1->SetLineColor(kRed);
  h1->Draw();
  
  TCanvas *c1 = new TCanvas("c1", "Fair Dice Distribution in 60000 rolls", 100, 10, 600, 600);
  c1->SetGrid();
  c1->GetFrame()->SetFillColor(10);
  c1->GetFrame()->SetBorderSize(1);
  c1->Divide(2,1);
  
  c1->cd(1);
  h2->SetLineColor(kGreen);
  h2->Draw();
  
  c1->cd(2);
  h3->SetLineColor(kBlue);
  h3->Draw();
  
  }
