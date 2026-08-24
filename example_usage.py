from client import LuxuryDesignerFashionPopUpTrunkShowClient

def main():
    client = LuxuryDesignerFashionPopUpTrunkShowClient()
    res = client.curate_vip_couture_trunk_show('Sabyasachi Heritage Collection')
    print('Trunk Show: ' + res['trunk_show_id'] + ' | Label: ' + res['designer_label'])
    print('Average Order Value: INR ' + str(res['average_ticket_value_inr']) + ' | Bespoke: ' + str(res['bespoke_made_to_order_cleared']))
    print('Global Tour: ' + ', '.join(res['global_private_trunk_show_cities']))

if __name__ == '__main__':
    main()
