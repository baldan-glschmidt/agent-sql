# R110IMG

## Descrição

Ficha Médica - Documentos

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodFic | Number(009,0) | Não | Ficha Médica |
| SeqFic | Number(003,0) | Não | Sequência do Documento |
| DesImg | String(030) | Sim | Descrição do Documento |
| Imagem | Image | Sim | Imagem |
| AnoImg | String(700) | Sim | Anotações do Documento |
| NomArq | String(250) | Sim | Nome do Arquivo |
| SitAss | Number(001,0) | Sim | Status da assinatura digital do documento |

---

## Chave Primária

- NumEmp
- CodFic
- SeqFic

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110IMG_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

