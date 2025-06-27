
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
  // out the probability of getting any of the six faces using histogram!

  {
  gROOT->Reset();
  #include "TMath.h"
  #include "TRandom.h"
  #include "TStyle.h"
  #include "TCanvas.h"
  
  TH1F *h1 = new TH1F("h1", "Face_1", 9, -1, 7);
  TH1F *h2 = new TH1F("h2", "Face_2", 9, -1, 7);
  TH1F *h3 = new TH1F("h3", "Face_3", 9, -1, 7);
  TH1F *h4 = new TH1F("h4", "Face_4", 9, -1, 7);
  TH1F *h5 = new TH1F("h5", "Face_5", 9, -1, 7);
  TH1F *h6 = new TH1F("h6", "Face_6", 9, -1, 7);
  


	TRandom r;
	r.SetSeed(0);
	ofstream out;
	out.open("Fair_Dice.out");
	
	int max = 1000000, entries = 10000;
	int T_all1 = 0, T_all2 = 0, T_all3 = 0, T_all4 = 0, T_all5 = 0, T_all6 = 0;
	
	for (int i = 0; i < entries; i++)
	{
	int kcount_even = 0, kcount_odd = 0;
	int T1 = 0, T2 = 0, T3 = 0, T4 = 0, T5 = 0, T6 = 0;
	out<<"face:"<<" face1"<<"\t"<<"face2"<<"\t"<<"face3"<<"\t"<<"face4"<<"\t"<<"face5"<<"\t"<<"face6"<<endl;
	
	     for (int j = 0; j < 6; j++)
	     {
	     int face1 = 0, face2 = 0, face3 = 0;
	     int face4 = 0, face5 = 0, face6 = 0;
	     
	     float x = r.Uniform(0, 1);
	     
	     	if (x < 1./6.)                      {face1++; T1++;}
	     	if (x > 1./6. && x < 2./6.)         {face2++; T2++;}
	     	if (x > 2./6. && x < 3./6.)         {face3++; T3++;}
	     	if (x > 3./6. && x < 4./6.)         {face4++; T4++;}
	     	if (x > 4./6. && x < 5./6.)         {face5++; T5++;}
	     	if (x > 5./6.)                      {face6++; T6++;}
	     
	     out<<"roll"<<j+1<<":"<<"\t"<<face1<<"\t"<<face2<<"\t"<<face3<<"\t"<<face4<<"\t"<<face5<<"\t"<<face6<<endl;
	     }
	     
	out<<".................................................................................."<<endl;
	out<<"total:"<<"\t"<<"\t"<<"total1"<<"\t"<<"total2"<<"\t"<<"total3"<<"\t"<<"total4"<<"\t"<<"total5"<<"\t"<<"total6"<<endl;
	out<<"all_six_rolls:"<<"\t"<<T1<<"\t"<<T2<<"\t"<<T3<<"\t"<<T4<<"\t"<<T5<<"\t"<<T6<<endl<<endl;
	     
        T_all1 += T1; T_all2 += T2;
	T_all3 += T3; T_all4 += T4;
	T_all5 += T5; T_all6 += T6;
	     
	     if (T1 > 0) h1->Fill(T1);       if (T2 > 0) h2->Fill(T2); 
	     if (T3 > 0) h3->Fill(T3);       if (T4 > 0) h4->Fill(T4); 
	     if (T5 > 0) h5->Fill(T5);       if (T6 > 0) h6->Fill(T6); 
	}
	
	kcount_odd = T_all1 + T_all3 + T_all5;
	kcount_even = T_all3 + T_all4 + T_all6;
	
	out<< "total number of rolls: " << entries*6<<endl;
	out<< "number of times face1: " <<T_all1<<endl;
	out<< "number of times face2: " <<T_all2<<endl;
	out<< "number of times face3: " <<T_all3<<endl;
	out<< "number of times face4: " <<T_all4<<endl;
	out<< "number of times face5: " <<T_all5<<endl;
	out<< "number of times face6: " <<T_all6<<endl;
	
	out<< "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"<<endl;
	out<< "total odd faces:  " <<kcount_odd<<endl;
	out<< "total even faces: " <<kcount_even<<endl;
	
  TCanvas *c1 = new TCanvas("c1", "Fair Dice Distribution in 60000 rolls", 100, 10, 600, 600);
  c1->SetGrid();
  c1->GetFrame()->SetFillColor(5);
  c1->GetFrame()->SetBorderSize(1);
  c1->Divide(2, 3);
  
  h1->SetXTitle("Dice Number Range");
  h1->SetYTitle("Frequency");
  
  
  c1->cd(1);
  h1->SetLineColor(kRed);
  h1->Draw();
  
  c1->cd(3);
  h3->SetLineColor(kGreen);
  h3->Draw();
  
  c1->cd(5);
  h5->SetLineColor(kBlue);
  h5->Draw();
  
  c1->cd(2);
  h2->SetLineColor(kBlack);
  h2->Draw();
  
  c1->cd(4);
  h4->SetLineColor(kViolet);
  h4->Draw();
  
  c1->cd(6);
  h6->SetLineColor(kOrange);
  h6->Draw();
  }
  
   
	
	
	
	
	    
	 
	     
	     
	     
