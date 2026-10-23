# R204PER

## Descrição

Período de Licença Especial

---

## Resumo

- Campos: 17
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| SeqPer | Number(003,0) | Não | Sequência Período |
| IniPer | Date | Sim | Data Início do Período |
| FimPer | Date | Sim | Data Fim do Período |
| DliDir | Number(006,2) | Sim | Dias de Direito |
| DliFal | Number(006,2) | Sim | Dias de Falta |
| DliPda | Number(006,2) | Sim | Dias Acumulados para Perda |
| DliDeb | Number(006,2) | Sim | Dias de Débito |
| DliSld | Number(006,2) | Sim | Dias de Saldo |
| DliPro | Number(006,2) | Sim | Dias de Prorrogação |
| AvoLic | Number(003,0) | Sim | Avos de Licença Especial |
| SitLic | Number(001,0) | Sim | Situação do Período |
| AltFim | String(001) | Sim | Alterou final do período |
| PerSus | String(001) | Sim | Período Está Suspenso |
| DiaSus | Number(006,2) | Sim | Dias de Suspensão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R204PER_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

