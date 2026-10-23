# R202RES

## Descrição

Teste Certificação - Respostas

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
| GruPer | Number(005,0) | Não | Código do Teste |
| CodPer | Number(003,0) | Não | Código da Pergunta |
| CodRes | Number(002,0) | Não | Código da Resposta |
| DesRes | String(1000) | Sim | Descrição da Resposta |
| ResEqv | String(030) | Sim | Abrangência das Resposta Equivalentes |
| ResCor | String(001) | Sim | Reposta Correta |
| AbrEmp | String(200) | Sim | Abrangência de Empresa |
| AbrFil | String(200) | Sim | Abrangência de filial |
| AbrLoc | String(1500) | Sim | Abrangência de local |
| AbrCar | String(100) | Sim | Abrangência de cargo |
| AbrTur | String(025) | Sim | Abrangência nos Turnos |
| TipACa | String(001) | Sim | Tipo de Abrangência do Campo |

---

## Chave Primária

- GruPer
- CodPer
- CodRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R202RES_001

**Tabela:** R202PER

| Origem | Destino |
|--------|---------|
| GruPer | GruPer |
| CodPer | CodPer |

