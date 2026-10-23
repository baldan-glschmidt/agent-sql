# R070BLC

## Descrição

Bloqueio de Crachás

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | Number(012,0) | Não | Número do Crachá |
| DatBlo | Date | Não | Data do Bloqueio do Acesso |
| HorBlo | Number(005,0) | Não | Hora do Bloqueio do Acesso |
| CodMot | Number(002,0) | Sim | Código do Motivo do Bloqueio |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Bloqueou/Liberou o Crachá |
| DatLib | Date | Sim | Data de Liberação |
| HorLib | Number(005,0) | Sim | Hora de Liberação |
| ObsBlo | String(080) | Sim | Observação Bloqueio/Liberação |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |

---

## Chave Primária

- NumCra
- DatBlo
- HorBlo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070BLC_003

**Tabela:** R070MBL

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

