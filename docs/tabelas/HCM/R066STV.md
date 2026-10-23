# R066STV

## Descrição

Status de Verificação do Dia

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Cadastro do Colaborador |
| DatApu | Date | Não | Data da Apuração do Colaborador |
| TexRet | String(2500) | Sim | Texto para retornar o comentário no processo BPM |
| ProcId | Number(009,0) | Sim | ID do processo no BPM |
| VerPro | Number(009,0) | Sim | Versão do processo no BPM |
| InstId | Number(009,0) | Sim | ID da instância do processo no BPM |
| BusDat | String(032) | Sim | UUID gerado no disparo para cruzar o callback BPM |
| TipSta | Number(001,0) | Sim | Status do processo BPM da verificação do dia |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
