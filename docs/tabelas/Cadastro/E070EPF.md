# E070EPF

## Descrição

Cadastros - Empresas - Parâmetros Fiscais

---

## Resumo

- Campos: 28
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| ParCpr | Number(001,0) | Sim | Parâmetro de configuração do código fiscal do produto |
| ParDpr | Number(001,0) | Sim | Parâmetro de configuração da descrição fiscal do produto |
| ParCse | Number(001,0) | Sim | Parâmetro de configuração do código fiscal do serviço |
| ParDse | Number(001,0) | Sim | Parâmetro de configuração da descrição fiscal do serviço |
| DupFis | String(001) | Sim | Permitir duplicar código fiscal |
| ManFis | String(001) | Sim | Permitir alterar código e descrição fiscal |
| UtiFis | String(001) | Sim | Utiliza código e descrição fiscal nas obrigações fiscais |
| DatHfi | Date | Sim | Competência para controle das alterações do produto/serviço por filial |
| BloAli | String(001) | Sim | Bloquear Edição Alíquota Tabela de Preço por Estado. |
| CtaPro | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos para produtos - Descontinuado |
| CtaSer | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos para serviços - Descontinuado |
| EntPro | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos com busca no cadastro de produtos para entradas |
| EntSer | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos com busca no cadastro de serviços para entradas |
| EntFam | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos com busca no cadastro de famílias para entradas |
| EntTns | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos com busca no cadastro de transações para entradas |
| EntDep | Number(002,0) | Sim | Origem da conta contábil na gestão de tributo com busca no cadastro de depósitos para entradas |
| SaiPro | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos com busca no cadastro de produtos para saídas |
| SaiSer | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos com busca no cadastro de serviços para saídas |
| SaiFam | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos com busca no cadastro de famílias para saídas |
| SaiTns | Number(002,0) | Sim | Origem da conta contábil na gestão de tributos com busca no cadastro de transações para saídas |
| SaiDep | Number(002,0) | Sim | Origem da conta contábil na gestão de tributo com busca no cadastro de depósitos para saídas |
| EntSeq | String(050) | Sim | Hash para busca da conta contábil para entradas |
| SaiSeq | String(050) | Sim | Hash para busca da conta contábil para saídas |
| OriPdf | Number(002,0) | Sim | Origem detalhamento da carga tributária nos documentos fiscais (Lei 12.741/12) |
| RegIrr | Number(001,0) | Sim | Regime Gross UP para cálculo de IRRF/PIS/COFINS Fornecedor Exterior |
| PrtSpd | String(001) | Sim | Gerar participante único para SPED Fiscal e Contribuições |
| CodBan | String(003) | Sim | Código do Banco conforme tabela BACEN |

---

## Chave Primária

- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070EPF_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

