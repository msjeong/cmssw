import FWCore.ParameterSet.Config as cms

#
# module to produce pixel seeds for electrons from super clusters
# Author:  Ursula Berthon, Claude Charlot
#
from RecoEgamma.EgammaElectronProducers.ecalDrivenElectronSeedsParameters_cff import *

ecalDrivenElectronSeeds = cms.EDProducer("ElectronSeedProducer",
    barrelSuperClusters = cms.InputTag("particleFlowSuperClusterECAL:particleFlowSuperClusterECALBarrel"),
    endcapSuperClusters = cms.InputTag("particleFlowSuperClusterECAL:particleFlowSuperClusterECALEndcapWithPreshower"),
    SeedConfiguration = cms.PSet(
        ecalDrivenElectronSeedsParameters,
#        OrderedHitsFactoryPSet = cms.PSet(
#            ComponentName = cms.string('StandardHitPairGenerator'),
#            SeedingLayers = cms.string('MixedLayerPairs') 
#        ),
#        TTRHBuilder = cms.string('WithTrackAngle'),
#        # eta-phi region
#        RegionPSet = cms.PSet(
#            deltaPhiRegion = cms.double(0.7),
#            originHalfLength = cms.double(15.0),
#            useZInVertex = cms.bool(True),
#            deltaEtaRegion = cms.double(0.3),
#            ptMin = cms.double(1.5),
#            originRadius = cms.double(0.2),
#            VertexProducer = cms.InputTag("pixelVertices")
#        )
    )
)


