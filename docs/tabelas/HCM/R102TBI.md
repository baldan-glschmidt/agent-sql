# R102TBI

## Descrição

Trabalhos do SESMT - Imagens

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTbr | Number(006,0) | Não | Código do Trabalho |
| SeqImg | Number(003,0) | Não | Sequência de imagem |
| DesImg | String(030) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Imagem |

---

## Chave Primária

- NumEmp
- CodTbr
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102TBI_001

**Tabela:** R102TBR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodTbr | CodTbr |

