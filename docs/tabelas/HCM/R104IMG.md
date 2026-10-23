# R104IMG

## Descrição

JR - Ações - Anexos

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| SeqImg | Number(003,0) | Não | Sequência da Imagem |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| DesImg | String(050) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Anexo |

---

## Chave Primária

- NumEmp
- CodPrc
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104IMG_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

