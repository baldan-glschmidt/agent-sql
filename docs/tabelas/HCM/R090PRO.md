# R090PRO

## Descrição

Procedimentos Tipo de Visita

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipVis | Number(003,0) | Não | Tipo da Visita |
| ProVis | Number(001,0) | Não | Tipo de Procedimento |
| ConPro | Number(001,0) | Não | Consistir Procedimento |
| GerOcp | String(001) | Sim | Gerar Incidente |
| TipOcP | Number(003,0) | Sim | Tipo do Incidente |
| ValVid | Number(003,0) | Sim | Qtde de Dias de Validade do Vídeo de Segurança |
| VisVau | String(001) | Sim | Visitado Autorizador |
| EmpLot | Number(004,0) | Sim | Empresa Lote |
| CodLot | Number(003,0) | Sim | Código do Lote |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Autorizador |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador do Autorizador |
| NumCad | Number(009,0) | Sim | Cadastro do Autorizador |

---

## Chave Primária

- TipVis
- ProVis
- ConPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090PRO_000

**Tabela:** R090TVI

| Origem | Destino |
|--------|---------|
| TipVis | TipVis |

