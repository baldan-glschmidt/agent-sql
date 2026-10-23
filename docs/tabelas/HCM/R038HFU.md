# R038HFU

## Descrição

Histórico Funções

---

## Resumo

- Campos: 21
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data de Início do Histórico de Função |
| SeqAlt | Number(002,0) | Não | Sequência do Histórico |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Função |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| DatFim | Date | Sim | Data Final do Histórico de Função |
| TipSbs | String(001) | Sim | Titular ou Substituto |
| TclSbs | Number(001,0) | Sim | Tipo do Substituído |
| CadSbs | Number(009,0) | Sim | Cadastro do Colaborador Substituído |
| DesObs | String(100) | Sim | Observação sobre este histórico |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| PerSbs | Number(009,5) | Sim | Percentual de Cálculo |
| MotAlt | Number(003,0) | Sim | Motivo da Alteração da Função |
| FunEso | String(001) | Sim | Função eSocial |
| IniEso | Date | Não | Data de Início no eSocial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- SeqAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038HFU_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HFU_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

