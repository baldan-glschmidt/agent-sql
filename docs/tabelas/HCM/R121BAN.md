# R121BAN

## Descrição

Concurso - Banca Examinadora

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| NumEmp | Number(004,0) | Não | Empresa do componente |
| TipCol | Number(001,0) | Não | Tipo do colabolador componente da banca |
| NumCad | Number(009,0) | Não | Cadastro do colaborador componente da banca |
| ObsBan | String(050) | Sim | Observação sobre o componente da banca |

---

## Chave Primária

- AnoCon
- NumCon
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121BAN_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

