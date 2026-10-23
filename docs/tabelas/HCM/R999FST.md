# R999FST

## Descrição

Configurações de performance das telas

---

## Resumo

- Campos: 16
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomFrm | String(030) | Não | Nome do form |
| CodUsu | Number(010,0) | Não | 0 Default, outro é uma configuração individual |
| FrmStt | Number(001,0) | Sim | Estado inicial  do form |
| RefEPK | String(001) | Sim | Atualizar dados ao sair do grupo chave |
| RefPst | String(001) | Sim | Atualizar dados ao confirmar inclusão/alteração de registro |
| RefCan | String(001) | Sim | Atualizar dados ao cancelar inclusão/&alteração de registro |
| RefDel | String(001) | Sim | Atualizar dados ao excluir registro |
| RefExF | String(001) | Sim | Atualizar dados de ligações ao sair dos campos |
| SngLSl | Number(005,0) | Sim | Buscar descrições de ligações com um único select |
| QueHin | Number(005,0) | Sim | Utilizar hints nos comandos SELECT |
| UseInd | String(001) | Sim | Usar hint para indicar índice nos comandos select |
| CloCur | Number(005,0) | Sim | Fechar cursores ao aguardar usuário |
| CloDel | Number(005,0) | Sim | Fecha cursores ao excluir registro (utilizado apenas em MS SQL Server 7.x e 2000) |
| AutCre | String(001) | Sim | Auto Create |
| NotDes | String(001) | Sim | Not Destroy |
| RowSet | Number(005,0) | Sim | RowSet size |

---

## Chave Primária

- NomFrm
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
