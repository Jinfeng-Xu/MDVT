import os
import argparse
from utils.quick_start import quick_start
os.environ['NUMEXPR_MAX_THREADS'] = '48'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', type=str, default='LGMRec_VP', help='name of models')
    parser.add_argument('--dataset', '-d', type=str, default='baby', help='name of datasets')
    parser.add_argument('--mg', default=False, action="store_true",
                        help='whether to use Mirror Gradient, default is False')
    parser.add_argument('--vp', type=str, default='2',
                        help='0: None, 1: Virtue Pairs, 2: Dynamic Virtue Pairs')

    config_dict = {
        'gpu_id': 0,
    }

    args, _ = parser.parse_known_args()

    quick_start(model=args.model, dataset=args.dataset, config_dict=config_dict, save_model=True, mg=args.mg, vp=args.vp)

