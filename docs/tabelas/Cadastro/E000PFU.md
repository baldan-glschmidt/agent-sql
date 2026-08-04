# E000PFU

## Descrição

Cadastros - Perfis de Usuário (Varejo)

---

## Resumo

- Campos: 59
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(009,0) | Não | Código do Perfil |
| DesPer | String(050) | Não | Descrição Perfil |
| RefPer | String(003) | Sim | Referência do Perfil |
| ObsPer | String(250) | Sim | Observação para o perfil |
| SitPer | String(001) | Não | Situação Perfil |
| DatGer | Date | Sim | Data da geração do perfil |
| HorGer | Number(005,0) | Sim | Hora da geração do perfil |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do perfil |
| McaPer | String(001) | Sim | Permissão para manter o cadastro de perfis de usuário |
| PrePro | String(001) | Sim | Permissão para reservar estoque de produtos |
| EreMan | String(001) | Sim | Permissão para exclusão de reservas manuais |
| PblEst | String(001) | Sim | Permissão para bloquear estoque |
| PdeEst | String(001) | Sim | Permissão para desbloquear estoque |
| PesMan | String(001) | Sim | Permissão para movimentar estoque manualmente |
| PreInv | String(001) | Sim | Permissão para realizar inventário |
| PtaVen | String(001) | Sim | Permissão para manter tabela de preço de venda |
| PgeNfe | String(001) | Sim | Permissão para gerar nota fiscal de entrada |
| PgeNfs | String(001) | Sim | Permissão para gerar nota fiscal de saída |
| PmoCif | String(001) | Sim | Permissão para movimentar contas internas financeiras |
| PapPed | String(001) | Sim | Permissão para aprovar pedido sem item obrigatório |
| PneTit | String(001) | Sim | Permissão para substituir/negociar títulos |
| PanCre | String(001) | Sim | Permissão para analisar crédito |
| PerMar | Number(005,2) | Sim | Percentual de negociação abaixo da margem de contribuição indicada |
| PfuTef | String(001) | Sim | Permissão para acessar funções administrativas do TEF |
| PfuEcf | String(001) | Sim | Permissão para acessar funções administrativas do ECF |
| PacInt | String(001) | Sim | Permissão para acessar função para forçar integração |
| PrePag | String(001) | Sim | Permissão para realizar pagamento |
| PreSan | String(001) | Sim | Permissão para realizar sangria |
| PreSup | String(001) | Sim | Permissão para realizar suprimento |
| PfeCxa | String(001) | Sim | Permissão para realizar fechamento de caixa |
| PcsCxa | String(001) | Sim | Permissão para consultar saldo do caixa |
| PcaIte | String(001) | Sim | Permissão para cancelar item da venda |
| PcaFis | String(001) | Sim | Permissão para cancelar a venda |
| PemRed | String(001) | Sim | Permissão para emitir redução Z |
| PabGav | String(001) | Sim | Permissão para abrir gaveta |
| LdeVen | Number(001,0) | Sim | Limitar desconto no total da venda |
| PedRec | Number(005,2) | Sim | Percentual de desconto permitido no recebimento |
| VdeRec | Number(015,2) | Sim | Valor de desconto permitido no recebimento |
| LdeTve | Number(001,0) | Sim | Limitar desconto no total da venda |
| PedTve | Number(005,2) | Sim | Percentual de desconto permitido no total da venda |
| VdeTve | Number(015,2) | Sim | Valor de desconto permitido no total da venda |
| LdeIve | Number(001,0) | Sim | Limitar desconto por item na venda |
| PedIve | Number(005,2) | Sim | Percentual de desconto permitido por item na venda |
| VdeIve | Number(015,2) | Sim | Valor de desconto permitido por item na venda |
| PalPAr | String(001) | Sim | Permissão para alterar parcelas |
| CanBti | String(001) | Sim | Permissão para cancelar baixa de títulos |
| AltFpg | String(001) | Sim | Permissão para alterar a forma de pagamento no PDV |
| CanTef | String(001) | Sim | Permissão para cancelar transação TEF Pendente |
| PerSer | Number(005,2) | Sim | Percentual permitido abaixo da meta de serviços |
| CadCli | String(001) | Sim | Indicativo se o operador pode cadastrar cliente |
| LdeRec | Number(001,0) | Sim | Tipo de limite a ser aplicado para desconto no recebimento |
| PerDsd | String(001) | Sim | Indicativo se permite efetuar uma devolução sem documento fiscal |
| AutDfp | String(001) | Não | Indica se pode autorizar dev. de mercadorias fora do período definido na filial |
| PadMco | String(001) | Sim | Permissão para Ativar/Desativar modo contingência |
| RecTvp | String(001) | Sim | Receber Título Vencido com Cheque Pré-Datado |
| AltJtv | String(001) | Sim | Alterar Juros/Multas/Descontos de Título vencido |
| TipAnf | Number(001,0) | Sim | Tipo de acesso a nota fiscal |
| PvoPfl | String(001) | Sim | Indicativo se permite efetuar a venda off-line de produtos fora de linha |
| PraCnr | String(001) | Sim | Permitir reprovação de análise de crédito no Retaguarda |

---

## Chave Primária

- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
