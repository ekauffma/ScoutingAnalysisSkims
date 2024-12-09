#include <memory>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"
#include "DataFormats/L1CaloTrigger/interface/CICADA.h"

using namespace std;

class CICADANtuplizer: public edm::one::EDAnalyzer< edm::one::SharedResources>
{
    public:
        explicit CICADANtuplizer(const edm::ParameterSet&);
        ~CICADANtuplizer() override = default;

    private:
        void beginJob() override {};
        void endJob() override {};

        void analyze(const edm::Event&, const edm::EventSetup&) override;

        edm::EDGetTokenT<l1t::CICADABxCollection> caloLayer1CICADAScoreToken_;
        edm::Service<TFileService> theFileService;

        TTree* outputTree;
        double cicadaScore;


};

CICADANtuplizer::CICADANtuplizer(const edm::ParameterSet& iConfig):
    caloLayer1CICADAScoreToken_(consumes<l1t::CICADABxCollection>(iConfig.getParameter<edm::InputTag>("caloLayer1CICADAScore")))
{
    usesResource("TFileService");
    outputTree = theFileService->make<TTree>("CICADA", "contains emulated CICADA score");
    outputTree->Branch("cicadaScore", &cicadaScore);
}

void CICADANtuplizer::analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)
{
    cicadaScore = (double)iEvent.get(caloLayer1CICADAScoreToken_)[0];
    outputTree->Fill();
}

DEFINE_FWK_MODULE(CICADANtuplizer);
