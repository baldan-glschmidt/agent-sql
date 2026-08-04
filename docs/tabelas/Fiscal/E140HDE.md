# E140HDE

## Descrição

Vendas - Notas Fiscais de Saída - Histórico de Documentos Eletrônicos

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| NumMan | Number(009,0) | Não | Número do manifesto |
| SeqHde | Number(004,0) | Não | Seqüência do histórico de documento eletrônicos |
| DesHde | String(1999) | Não | Texto da histórico de documentos eletrônicos |
| UsuGer | Number(009,0) | Sim | Usuário responsável pela entrada da observação |
| DatGer | Date | Sim | Data da observação |
| HorGer | Number(005,0) | Sim | Hora da observação |
| CodRej | Number(006,0) | Sim | Código da rejeição |
| MsgRej | String(1000) | Sim | Mensagem da rejeição |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- NumMan
- SeqHde

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
