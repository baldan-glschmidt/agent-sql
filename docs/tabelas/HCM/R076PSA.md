# R076PSA

## Descrição

Proposta de Alteração Salarial

---

## Resumo

- Campos: 32
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Cadastro |
| DatAlt | Date | Não | Data da Proposta |
| CodMot | Number(003,0) | Sim | Motivo da Proposta |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| PerDes | Number(005,2) | Sim | % de Desempenho |
| ValSal | Number(013,4) | Sim | Valor do Salário |
| CplSal | Number(013,4) | Sim | Valor do Complemento |
| TipSal | Number(001,0) | Sim | Tipo do Salário (Categoria) |
| SitPrp | Number(001,0) | Sim | Situação da Proposta |
| OriPrp | Number(001,0) | Sim | Origem da Proposta |
| VlrRes | Number(013,4) | Sim | Valor Residual |
| PerRea | Number(005,2) | Sim | % de Reajuste |
| DatEfe | Date | Sim | Data da Efetivação da Proposta |
| PerRes | Number(005,2) | Sim | % Residual |
| ObsPsa | String(1000) | Sim | Observação Proposta de Salário |
| NumLot | Number(009,0) | Sim | Número do lote de geração |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| EmpRsp | Number(004,0) | Sim | Código da Empresa do Responsável |
| TipRsp | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| CadRsp | Number(009,0) | Sim | Cadastro do Colaborador Responsável |
| ValOri | Number(013,4) | Sim | Valor original do salário da proposta quando ocorrer reajuste salarial |
| USU_CodMot | Number(003,0) | Sim | Código do Motivo da Proposta |
| USU_CadDir | Number(009,0) | Sim | Diretor Responsável |
| USU_TipDir | Number(001,0) | Sim | Tipo Diretor |
| USU_RetAfa | Date | Sim | Retorno do Afastamento |
| USU_SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| USU_Setor | String(030) | Sim | Setor |
| USU_CodCcu | String(018) | Sim | Código Centro de Custo Contábil |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R076PSA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R076PSA_004

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

