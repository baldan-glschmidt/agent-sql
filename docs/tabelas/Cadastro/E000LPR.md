# E000LPR

## Descrição

Tabelas - Lista de Presentes

---

## Resumo

- Campos: 17
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeLpr | Number(009,0) | Não | Número da lista de presente |
| CodEmp | Number(004,0) | Não | Código da empresa |
| FilCad | Number(005,0) | Não | Código da filial responsável pelo cadastro |
| TipLst | Number(002,0) | Sim | Tipo da lista de presentes |
| DesLst | String(250) | Não | Descrição da lista de presentes |
| CliPrc | Number(009,0) | Sim | Código do cliente principal da lista |
| CliSec | Number(009,0) | Sim | Código do cliente secundário da lista |
| DatEve | Date | Sim | Data de realização do evento |
| HorEve | Number(005,0) | Sim | Hora de realização do evento |
| DatVfl | Date | Sim | Data de validade da lista |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| QtdCon | Number(009,0) | Sim | Quantidade de convidados para o evento |
| LocEve | String(250) | Não | Local onde será realizado o evento |
| ObsAdi | String(999) | Sim | Observações adicionais |
| SitLpr | String(001) | Sim | Situação da lista de presente (Ativa ou Inativa) |

---

## Chave Primária

- IdeLpr

---

## Índices

### E000LPRIndice1

**Tipo:** Não unico

Campos:
- CliPrc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
