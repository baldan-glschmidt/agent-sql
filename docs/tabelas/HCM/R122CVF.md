# R122CVF

## Descrição

Candidatos Externos - Currículo Formatado

---

## Resumo

- Campos: 3
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| CvfCan | String(40000) | Sim | Currículo do candidato com formatação básica |
| TxtCvf | String(9000) | Sim | Texto extraído do currículo formatado |

---

## Chave Primária

- NumCan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CVF_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

