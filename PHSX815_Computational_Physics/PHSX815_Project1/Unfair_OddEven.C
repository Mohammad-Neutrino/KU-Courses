
  //////////////////////////////////////////////
  //                                          //
  //   Code by: Mohammad Ful Hossain Seikh    //
  //   @University of Kansas, USA             //
  //   February 26, 2021                      //
  //   Project1                               //
  //   Computational Physics PHSX 815         //
  //                                          //
  //////////////////////////////////////////////


  // Construction of an UnFair Dice
  // The goal is to construct an unfair dice (even faces twice as likely as odd faces) of six faces using 
  // random numbers and find out the probability of getting odd and even faces using histogram!
  
  {
  gROOT->Reset();
  #include "TMath.h"
  #include "TRandom.h"
  #include "TStyle.h"
  #include "TCanvas.h"

  TH1F *h1 = new TH1F("h1", "Unfair Uniform Distribution", 100, -2, 3);
  TH1F *h2 = new TH1F("h2", "Unfair Even Distribution", 6, -1, 5);
  TH1F *h3 = new TH1F("h3", "Unfair Odd Distribution", 6, -1, 5);
  h1->SetXTitle("Interval");
  h1->SetYTitle("Frequency");
  
    TRandom r;
    r.SetSeed(0);
    ofstream out;
    out.open("Unfair_OddEven.out");

    int max = 1000000, entries = 10000;
    int kcount = 0, sum_kcount_even = 0, sum_kcount_odd = 0;
    
    
    out<<"attempt"<<"  "<<"Even"<<"  "<<"Odd"<<"  "<<"Total_Even"<<"  "<<"Total_Odd"<<endl;
    for (int i = 0; i < entries; i++)
    {
    int kcount_even = 0, kcount_odd = 0;
 
       for (int j = 0; j < 3; j++)
       {
       float x = r.Uniform(0, 1);
       int y = 3*x + 2;
       h1->Fill(x);
       
           if (y%2 == 0)
           {
           kcount_even++;
           sum_kcount_even++;
           }
           
           if (y%2 == 1)
           {
           kcount_odd++;
           sum_kcount_odd++;
           }
           
       }
       
       h2->Fill(kcount_even);
       h3->Fill(kcount_odd);
       
       out<<i<<"\t"<<kcount_even<<"\t"<<kcount_odd<<" \t"<<sum_kcount_even<<"\t"<<sum_kcount_odd<<endl;
       
    }
  
    out<< "total number of rolls: " <<entries*3<<endl;
    out<< "Even Probability: " <<float(sum_kcount_even)/entries<<endl;
    out<< "Odd Probability:  " <<float(sum_kcount_odd)/entries<<endl;
    
   
  TCanvas *c2 = new TCanvas("c2", "Unfair Dice Odd Even", 100, 10, 600, 600);
  c2->cd();
  c2->SetGrid();
  h1->SetLineColor(kRed);
  h1->Draw();
  
  TCanvas *c1 = new TCanvas("c1", "Fair Dice Distribution in 60000 rolls", 100, 10, 500, 400);
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


       
           
           


