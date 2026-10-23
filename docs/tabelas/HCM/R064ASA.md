# R064ASA

## Descrição

Autorização de Saída

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAsa | Date | Não | Data da Autorização de Saída |
| HorAsa | Number(005,0) | Não | Hora da Autorização de Saída |
| HorTer | Number(005,0) | Sim | Hora do Término da Autorização de Saída |
| CodSit | Number(003,0) | Sim | Código da Situação |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador da Saída |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador da Saída |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador da Saída |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Autorização |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| ObsAsa | String(100) | Sim | Observação de Horas Extras |
| USU_MOTIVO | String(001) | Sim | Motivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAsa
- HorAsa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064ASA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

