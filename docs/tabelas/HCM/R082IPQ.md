# R082IPQ

## Descrição

Produtos Químicos - Imagens

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPro | Number(006,0) | Não | Código do Produto Químico |
| SeqImg | Number(003,0) | Não | Sequência da Imagem |
| NomArq | String(250) | Sim | Nome do anexo de anexo |
| DesImg | String(060) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Imagem |

---

## Chave Primária

- CodPro
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R082IPQ_000

**Tabela:** R082PRO

| Origem | Destino |
|--------|---------|
| CodPro | CodPro |

