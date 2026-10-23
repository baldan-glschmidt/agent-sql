# R103IMG

## Descrição

PSS - Inspeções - Imagens

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPss | Number(003,0) | Não | Código do grupo de PSS |
| CodIns | Number(004,0) | Não | Número da Inspeção |
| SeqImg | Number(003,0) | Não | Sequência de imagem |
| DesImg | String(030) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Imagem |

---

## Chave Primária

- NumEmp
- CodPss
- CodIns
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R103IMG_001

**Tabela:** R103GPS

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPss | CodPss |

