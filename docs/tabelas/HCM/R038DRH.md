# R038DRH

## Descrição

Histórico Postos de Trabalho - Delegação de responsabilidades da Hierarquia do Posto

---

## Resumo

- Campos: 15
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| IniAtu | Date | Não | Início da atuação do Colaborador no Posto de trabalho |
| SeqHis | Number(002,0) | Não | Sequência do Histórico |
| CodThp | Number(003,0) | Não | Indica a hierarquia em que se deseja registrar a delegação |
| IniDel | Date | Não | Define a data de início da delegação |
| EmpDel | Number(004,0) | Sim | Empresa do colaborador que recebe a delegação |
| TipDel | Number(001,0) | Sim | Tipo do colaborador que recebe a delegação |
| CadDel | Number(009,0) | Sim | Cadastro do colaborador que recebe a delegação |
| ValDel | Number(001,0) | Sim | Permite definir a validade da delegação da responsabilidade |
| TerDel | Date | Sim | Define a data de término da delegação |
| ObsDel | String(2000) | Sim | Observação da delegação da responsabilidade |
| CodUsu | Number(009,0) | Sim | Usuário responsável pela última alteração do registro de delegação |
| DthAlt | Number(014,6) | Sim | Data e hora da última alteração no registro da delegação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniAtu
- SeqHis
- CodThp
- IniDel

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038DRH_004

**Tabela:** R038HPO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniAtu | IniAtu |
| SeqHis | SeqHis |

### IR_R038DRH_005

**Tabela:** R017THP

| Origem | Destino |
|--------|---------|
| CodThp | CodThp |

