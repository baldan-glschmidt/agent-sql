# E001TIT

## Descrição

Tabelas - Transações - Títulos de Impostos

---

## Resumo

- Campos: 19
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqTit | Number(003,0) | Não | Seqüência de parâmetros para geração do título de imposto |
| TipImp | Number(002,0) | Sim | Tipo de imposto |
| CodImp | String(003) | Sim | Código do imposto para geração do título |
| ForTit | Number(009,0) | Sim | Código do fornecedor para geração do título de impostos |
| TipTit | String(003) | Sim | Tipo de título para geração do título de imposto |
| TnsTit | String(005) | Sim | Transação padrão para geração do título de imposto |
| FgeTif | Number(001,0) | Sim | Data do fato gerador para geração do título para pessoa física |
| FgeTij | Number(001,0) | Sim | Data do fato gerador para geração do título para pessoa jurídica |
| CodTri | String(005) | Sim | Código de tributação para emissão da DARF |
| CodTre | Number(004,0) | Sim | Tipo de remessa para o exterior do contrato de aplicação\captação de recursos |
| CodReg | Number(004,0) | Sim | Código da regra para geração do imposto |
| SitTit | String(001) | Sim | Situação da seqüência de parâmetros para geração do título de imposto |
| ObsTit | String(250) | Sim | Observação da seqüência de parâmetros para geração do título |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| DiaVct | Number(002,0) | Sim | Quantidade de dias após data apuração final para vencimento |
| AntPos | String(001) | Sim | Indicativo do critério de definição de vencimento do título a pagar |

---

## Chave Primária

- CodEmp
- CodTns
- CodFil
- SeqTit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
