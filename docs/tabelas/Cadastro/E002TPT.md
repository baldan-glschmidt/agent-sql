# E002TPT

## Descrição

Tabelas - Tipos de Título

---

## Resumo

- Campos: 22
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTpt | String(003) | Não | Código interno do tipo de título |
| DesTpt | String(040) | Não | Descrição do tipo de título |
| AbrTpt | String(005) | Não | Abreviatura do tipo de título |
| RecSom | String(001) | Não | Indicativo onde somar nos saldos dos históricos dos clientes |
| PagSom | String(001) | Não | Indicativo onde somar nos saldos dos históricos dos fornecedores |
| AplTpt | String(001) | Sim | Aplicação do tipo de título |
| VenCac | String(001) | Não | Indicativo se tipo é considerado  para análise de crédito de pedido e NF |
| SomIrf | String(001) | Sim | Indicativo se  o tipo de título soma para base Imposto e gera título na baixa |
| PagEev | Number(003,0) | Sim | Quantidade mínima de dias aceito entre a data de entrada e o vencimento de um título |
| CodPdv | Number(004,0) | Sim | Código interno no PDV |
| GerDct | String(001) | Sim | Gera declaração de débitos e créditos tributários federais (DCTF) |
| CodImp | String(003) | Sim | Código do imposto |
| TitFis | Number(002,0) | Não | Tipo de título fiscal |
| SitTpt | String(001) | Sim | Indicativo da situação do tipo de título |
| ExcVar | String(001) | Não | Indica se o uso deste tipo de título é exclusivo do sistema de varejo |
| GerRgw | String(001) | Sim | Indica se o tipo de título gerará o registro adicional W para imposto |
| TitPar | String(001) | Sim | Indicativo para manter o número do título da parcela ao gerar Contas a Receber |
| IntAcp | String(001) | Sim | Habilitar integração com Antecipação Contas a Pagar |
| EneLpr | Number(001,0) | Sim | Enquadramento especial no LCDPR |
| PerIrm | Number(004,2) | Sim | Percentual de IR para contrato de mútuo |
| PerIld | Number(004,2) | Sim | Percentual de IR para Lucros e Dividendos |
| VlrIld | Number(015,2) | Sim | Valor limite de isenção de IR para Lucros e Dividendos |

---

## Chave Primária

- CodTpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
