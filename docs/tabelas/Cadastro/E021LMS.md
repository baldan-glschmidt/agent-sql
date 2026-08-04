# E021LMS

## Descrição

Tabelas - Liga Motivos e Aplicações a Possíveis Soluções

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AplMot | Number(002,0) | Não | Aplicação dos motivos das situações das tabelas |
| CodMot | Number(006,0) | Não | Código do motivo da observação ou situação |
| CodSlc | String(003) | Não | Possível solução para o motivo |
| UsuGer | Number(010,0) | Sim | Usuário Responsável pela Geração do Registro |

---

## Chave Primária

- AplMot
- CodMot
- CodSlc

---

## Índices

### E021LMSIndice1

**Tipo:** Não unico

Campos:
- CodMot

### E021LMSIndice2

**Tipo:** Não unico

Campos:
- CodSlc

---

## Relacionamentos

### IR_E021LMS_001

**Tabela:** E021MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

### IR_E021LMS_002

**Tabela:** E021SLC

| Origem | Destino |
|--------|---------|
| CodSlc | CodSlc |

