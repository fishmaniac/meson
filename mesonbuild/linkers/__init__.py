# Copyright 2012-2021 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .detect import (
    defaults,
    guess_win_linker,
    guess_nix_linker,
)
from .linkers import (
    RSPFileSyntax,

    StaticLinker,
    VisualStudioLikeLinker,
    VisualStudioLinker,
    IntelVisualStudioLinker,
    AppleArLinker,
    ArLinker,
    ArmarLinker,
    DLinker,
    CcrxLinker,
    Xc16Linker,
    CompCertLinker,
    C2000Linker,
    TILinker,
    AIXArLinker,
    PGIStaticLinker,
    NvidiaHPC_StaticLinker,
    MetrowerksStaticLinker,
    MetrowerksStaticLinkerARM,
    MetrowerksStaticLinkerEmbeddedPowerPC,

    DynamicLinker,
    PosixDynamicLinkerMixin,
    GnuLikeDynamicLinkerMixin,
    AppleDynamicLinker,
    GnuDynamicLinker,
    GnuGoldDynamicLinker,
    GnuBFDDynamicLinker,
    LLVMDynamicLinker,
    MoldDynamicLinker,
    WASMDynamicLinker,
    CcrxDynamicLinker,
    Xc16DynamicLinker,
    CompCertDynamicLinker,
    C2000DynamicLinker,
    TIDynamicLinker,
    ArmDynamicLinker,
    ArmClangDynamicLinker,
    QualcommLLVMDynamicLinker,
    PGIDynamicLinker,
    NvidiaHPC_DynamicLinker,
    NAGDynamicLinker,
    MetrowerksLinker,
    MetrowerksLinkerARM,
    MetrowerksLinkerEmbeddedPowerPC,

    VisualStudioLikeLinkerMixin,
    MSVCDynamicLinker,
    ClangClDynamicLinker,
    XilinkDynamicLinker,
    SolarisDynamicLinker,
    AIXDynamicLinker,
    OptlinkDynamicLinker,
    CudaLinker,

    prepare_rpaths,
    order_rpaths,
    evaluate_rpath,
)

__all__ = [
    # detect.py
    'defaults',
    'guess_win_linker',
    'guess_nix_linker',

    # linkers.py
    'RSPFileSyntax',

    'StaticLinker',
    'VisualStudioLikeLinker',
    'VisualStudioLinker',
    'IntelVisualStudioLinker',
    'ArLinker',
    'ArmarLinker',
    'DLinker',
    'CcrxLinker',
    'Xc16Linker',
    'CompCertLinker',
    'C2000Linker',
    'TILinker',
    'AIXArLinker',
    'AppleArLinker',
    'PGIStaticLinker',
    'NvidiaHPC_StaticLinker',
    'MetrowerksStaticLinker',
    'MetrowerksStaticLinkerARM',
    'MetrowerksStaticLinkerEmbeddedPowerPC',

    'DynamicLinker',
    'PosixDynamicLinkerMixin',
    'GnuLikeDynamicLinkerMixin',
    'AppleDynamicLinker',
    'GnuDynamicLinker',
    'GnuGoldDynamicLinker',
    'GnuBFDDynamicLinker',
    'LLVMDynamicLinker',
    'MoldDynamicLinker',
    'WASMDynamicLinker',
    'CcrxDynamicLinker',
    'Xc16DynamicLinker',
    'CompCertDynamicLinker',
    'C2000DynamicLinker',
    'TIDynamicLinker',
    'ArmDynamicLinker',
    'ArmClangDynamicLinker',
    'QualcommLLVMDynamicLinker',
    'PGIDynamicLinker',
    'NvidiaHPC_DynamicLinker',
    'NAGDynamicLinker',
    'MetrowerksLinker',
    'MetrowerksLinkerARM',
    'MetrowerksLinkerEmbeddedPowerPC',

    'VisualStudioLikeLinkerMixin',
    'MSVCDynamicLinker',
    'ClangClDynamicLinker',
    'XilinkDynamicLinker',
    'SolarisDynamicLinker',
    'AIXDynamicLinker',
    'OptlinkDynamicLinker',
    'CudaLinker',

    'prepare_rpaths',
    'order_rpaths',
    'evaluate_rpath',
]
