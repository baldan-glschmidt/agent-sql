# R400ABR

## Descrição

Abrangência da Replicação das Tabelas

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomTab | String(010) | Não | Nome da Tabela |
| NomCam | String(010) | Não | Nome do Campo da Tabela |
| TipACa | String(001) | Sim | Tipo de Abrangência do Campo |
| AbrCam | String(100) | Sim | Abrangência do Campo para Replicação |

---

## Chave Primária

- NomTab
- NomCam

---

## Índices

### R400ABRIndice2

**Tipo:** Não unico

Campos:
- NomCam

---

## Relacionamentos

### IR_R400ABR_000

**Tabela:** R400TAB

| Origem | Destino |
|--------|---------|
| NomTab | NomTab |

